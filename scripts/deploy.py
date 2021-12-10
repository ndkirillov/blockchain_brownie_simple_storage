from brownie import accounts, config, StorageContract, network


def deploy_simple_storage():
    account = accounts[0]
    # account = accounts.load("test")
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = StorageContract.deploy({"from": account})
    stored_value = simple_storage.viewStateVar()
    print(stored_value)
    transaction_update = simple_storage.store(15, {"from": account})
    transaction_update.wait(1)
    updated_value = simple_storage.viewStateVar()
    print(updated_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
