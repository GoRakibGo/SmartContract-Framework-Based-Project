from brownie import SimpleStorage, accounts, config

def read_contaract():
    simple_storage = SimpleStorage[-1]
    # go take the index thats one less than the length
    # ABI
    # Address
    print(simple_storage.retrieve())

def main():
    read_contaract()