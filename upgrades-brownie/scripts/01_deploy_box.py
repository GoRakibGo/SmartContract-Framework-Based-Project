from scripts.helpful_scripts import get_account
from brownie import Box, BoxV2, ProxyAdmin, TransparentUpgradeableProxy, Contract
import eth_utils

def deploy_box():
    account = get_account()
    box = Box.deploy({"from": account})
    print(box.address)
    proxy_admin = ProxyAdmin.deploy({"from": account})
    initializer = eth_utils.to_bytes(hexstr= "0x")
    proxy = TransparentUpgradeableProxy.deploy(
        box.address, proxy_admin.address, initializer, 
        {"from": account, "gas_limit": 1000000},
    )
    print(f"Proxy deploye to {proxy}! you  can now upgrades!")
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    print(f"{proxy_box.retrieve()}")
    tx = proxy_box.store(77, {"from": account})
    tx.wait(1)
    print(f"{proxy_box.retrieve()}")

def upgrade_box():
    account = get_account()
    box_v2 = BoxV2.deploy({"from": account})
    proxy = TransparentUpgradeableProxy[-1]
    proxy_admin = ProxyAdmin[-1]
    tx = proxy_admin.upgrade(proxy.address, box_v2.address, {"from": account})
    tx.wait(1)
    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)
    tx = proxy_box.increment({"from": account})
    tx.wait(1)
    print(f"{proxy_box.retrieve()}")


def main():
    deploy_box()
    upgrade_box()