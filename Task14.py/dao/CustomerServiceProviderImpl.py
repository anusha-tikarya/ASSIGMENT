from dao.ICustomerServiceProvider import ICustomerServiceProvider
from entity.transaction import Transaction
from entity.account import SavingsAccount,CurrentAccount,ZeroBalanceAccount
from util.DBconn import DBConnection
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.db = DBConnection()

    def get_account_balance(self, account_number):
        account = self.get_account_details(account_number)
        if account:
            return account['Balance']
        else:
            raise ValueError("Account not found")

    def deposit(self, account_number, amount):
        account = self.get_account_details(account_number)
        if account:
            new_balance = account['Balance'] + amount
            self.db.execute_query("UPDATE Accounts SET Balance = ? WHERE AccountNumber = ?", (new_balance, account_number))
            return new_balance
        else:
            raise ValueError("Account not found")

    def withdraw(self, account_number, amount):
        account = self.get_account_details(account_number)
        if account:
            if account['AccountType'] == "Savings" and account['Balance'] - amount < 500:
                raise ValueError("Cannot withdraw: Minimum balance requirement")
            elif account['AccountType'] == "Current" and account['Balance'] - amount < -account['OverdraftLimit']:
                raise ValueError("Cannot withdraw: Overdraft limit exceeded")
            else:
                new_balance = account['Balance'] - amount
                self.db.execute_query("UPDATE Accounts SET Balance = ? WHERE AccountNumber = ?", (new_balance, account_number))
                return new_balance
        else:
            raise ValueError("Account not found")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account_details(from_account_number)
        to_account = self.get_account_details(to_account_number)
        if from_account and to_account:
            self.withdraw(from_account_number, amount)
            self.deposit(to_account_number, amount)
        else:
            raise ValueError("One or both accounts not found")

    def get_account_details(self, account_number):
        account = self.db.fetchone("SELECT * FROM Accounts WHERE AccountNumber = ?", (account_number,))
        if account:
            return {
                "AccountNumber": account.AccountNumber,
                "AccountType": account.AccountType,
                "Balance": account.Balance,
                "CustomerID": account.CustomerID,
                "InterestRate": account.InterestRate,
                "OverdraftLimit": account.OverdraftLimit,
            }
        else:
            return None

    def get_transactions(self, account_number, from_date, to_date):
        transactions = self.db.fetchall(
            "SELECT * FROM Transactions WHERE AccountNumber = ? AND DateTime BETWEEN ? AND ?",
            (account_number, from_date, to_date)
        )
        return transactions