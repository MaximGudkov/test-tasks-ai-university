from datetime import datetime


class Transaction:
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    INTEREST = "INTEREST"

    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.date = datetime.now()
        self.transaction_type = transaction_type
