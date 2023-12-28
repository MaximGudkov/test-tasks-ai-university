from banksystem.client import Client

# Создаем клиента
client = Client("Иван")

# Создаем различные счета для клиента
client.create_account("Savings", 10)
client.create_account("Credit", limit=5000, interest_rate=5)
client.create_account("Current")

# Вносим деньги на счета
client.accounts[0].deposit(1000)
client.accounts[1].deposit(2000)
client.accounts[2].deposit(1500)

# Просматриваем баланс и историю транзакций
for account in client.accounts:
    account.check_balance()
    account.view_transactions()

# Снимаем деньги с кредитного счета
client.accounts[1].withdraw(1000)

# Просматриваем баланс и историю транзакций после снятия
client.accounts[1].check_balance()
client.accounts[1].view_transactions()

# Рассчитываем проценты по сберегательному счету
client.accounts[0].calculate_interest()

# Просматриваем баланс и историю транзакций после начисления процентов
client.accounts[0].check_balance()
client.accounts[0].view_transactions()
