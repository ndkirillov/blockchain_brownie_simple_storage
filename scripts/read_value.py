from brownie import StorageContract, accounts, config


def read_contract():
    simple_storage = StorageContract[-1]
    print(simple_storage.viewStateVar)


def main():
    read_contract()
