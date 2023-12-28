from .utils.logger import logger

from .accounts import SavingsAccount, CreditAccount, Account


class Client:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, account_type, *args, **kwargs):
        if account_type == "Savings":
            account = SavingsAccount(*args, **kwargs)
        elif account_type == "Credit":
            account = CreditAccount(*args, **kwargs)
        else:
            account = Account(account_type)
        self.accounts.append(account)
        logger.info(f"{self.name}, создан новый счет типа {account_type}")
