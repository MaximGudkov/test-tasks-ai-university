from decimal import Decimal

from .utils.logger import logger
from .utils.decimal_config import convert_to_decimal
from .transaction import Transaction


class Account:
    def __init__(self, account_type):
        self.balance = Decimal("0.00")
        self.transactions = []
        self.account_type = account_type

    def _round_balance(self):
        self.balance = round(self.balance, 2)

    def _add_transaction(self, amount, transaction_type):
        self.transactions.append(Transaction(amount, transaction_type))

    def deposit(self, amount):
        amount = convert_to_decimal(amount)
        if amount > 0:
            self.balance += amount
            self._round_balance()
            self._add_transaction(amount, Transaction.DEPOSIT)
            logger.info(
                f"Внесено {amount} на счет {self.account_type}. Новый баланс: {self.balance}"
            )
        else:
            logger.error("Ошибка: Неверная сумма для внесения.")

    def withdraw(self, amount):
        amount = convert_to_decimal(amount)
        if 0 < amount <= self.balance:
            self._round_balance()
            self._add_transaction(amount, Transaction.WITHDRAW)
            logger.info(
                f"Снято {amount} со счета {self.account_type}. Новый баланс: {self.balance}"
            )
        else:
            logger.error(
                "Ошибка: Неверная сумма для снятия или недостаточно средств на счете."
            )

    def check_balance(self):
        logger.info(f"Текущий баланс: {self.balance}")

    def view_transactions(self):
        logger.info(f"История транзакций счёта {self.account_type}:")
        for transaction in self.transactions:
            logger.info(
                f"{transaction.date}: {transaction.transaction_type} на сумму {transaction.amount}"
            )


class InterestCalculatable:
    def __init__(self, interest_rate) -> None:
        self.interest_rate = Decimal(str(interest_rate))

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / Decimal(100))
        self.balance += interest
        self._round_balance()
        self._add_transaction(interest, Transaction.INTEREST)
        logger.info(f"Начислены проценты на счет {self.account_type}: {interest}. Новый баланс: {self.balance}")


class SavingsAccount(Account, InterestCalculatable):
    def __init__(self, interest_rate):
        super().__init__("Savings")
        InterestCalculatable.__init__(self, interest_rate)


class CreditAccount(Account, InterestCalculatable):
    def __init__(self, limit, interest_rate):
        super().__init__("Credit")
        self.limit = limit
        InterestCalculatable.__init__(self, interest_rate)

    def withdraw(self, amount):
        amount = convert_to_decimal(amount)
        if amount > 0 and (self.balance - amount) >= -self.limit:
            self.balance -= amount
            self._add_transaction(amount, Transaction.WITHDRAW)
            logger.info(
                f"Снято {amount} со счета {self.account_type}. Новый баланс: {self.balance}"
            )
        else:
            logger.error(
                "Ошибка: Неверная сумма для снятия или превышен лимит по кредиту."
            )
