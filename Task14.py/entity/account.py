class Account:
    lastAccNo = 0

    def __init__(self, account_type, account_balance, customer):
        Account.lastAccNo += 1
        self.account_number = Account.lastAccNo
        self.account_type = account_type
        self.account_balance = account_balance
        self.customer = customer

    def __str__(self):
        return f"Account[Number={self.account_number}, Type={self.account_type}, Balance={self.account_balance}, Customer={self.customer}]"

class SavingsAccount(Account):
    def __init__(self, account_balance, customer, interest_rate):
        super().__init__("Savings", max(account_balance, 500), customer)
        self.interest_rate = interest_rate

class CurrentAccount(Account):
    def __init__(self, account_balance, customer, overdraft_limit):
        super().__init__("Current", account_balance, customer)
        self.overdraft_limit = overdraft_limit

class ZeroBalanceAccount(Account):
    def __init__(self, customer):
        super().__init__("ZeroBalance", 0, customer)