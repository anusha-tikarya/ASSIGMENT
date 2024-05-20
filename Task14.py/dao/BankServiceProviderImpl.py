

from dao.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from dao.IBankServiceProvider import IBankServiceProvider
from util.DBconn import DBConnection
import datetime

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address
        self.db = DBConnection()

    def create_account(self, customer, acc_type, balance):
        customer_id = self.create_customer(customer)
        account_number = self.generate_account_number()

        if acc_type == "Savings":
            self.db.execute_query(
                "INSERT INTO Accounts (AccountNumber, AccountType, Balance, CustomerID, InterestRate) VALUES (?, ?, ?, ?, ?)",
                (account_number, acc_type, balance, customer_id, 0.04)
            )
        elif acc_type == "Current":
            self.db.execute_query(
                "INSERT INTO Accounts (AccountNumber, AccountType, Balance, CustomerID, OverdraftLimit) VALUES (?, ?, ?, ?, ?)",
                (account_number, acc_type, balance, customer_id, 1000)
            )
        elif acc_type == "ZeroBalance":
            self.db.execute_query(
                "INSERT INTO Accounts (AccountNumber, AccountType, Balance, CustomerID) VALUES (?, ?, ?, ?)",
                (account_number, acc_type, balance, customer_id)
            )
        else:
            raise ValueError("Invalid account type")
        
        return account_number

    def create_customer(self, customer):
        self.db.execute_query(
            "INSERT INTO Customers (CustomerID, Name, Address) VALUES (?, ?, ?)",
            (customer.customer_id, customer.name, customer.address)
        )
        return customer.customer_id

    def generate_account_number(self):
        result = self.db.fetchone("SELECT COALESCE(MAX(AccountNumber), 0) + 1 AS NextAccountNumber FROM Accounts")
        return result[0] if result else 1

    def list_accounts(self):
        accounts = self.db.fetchall("SELECT * FROM Accounts")
        return accounts

    def calculate_interest(self):
        savings_accounts = self.db.fetchall("SELECT AccountNumber, Balance, InterestRate FROM Accounts WHERE AccountType = 'Savings'")
        for account in savings_accounts:
            new_balance = account[1] + (account[1] * account[2])
            self.db.execute_query("UPDATE Accounts SET Balance = ? WHERE AccountNumber = ?", (new_balance, account[0]))

    def get_account_balance(self, account_number):
        query = "SELECT Balance FROM Accounts WHERE AccountNumber = ?"
        result = self.db.fetchone(query, (account_number,))
        return result[0] if result else None

    def deposit(self, account_number, amount):
        query = "UPDATE Accounts SET Balance = Balance + ? WHERE AccountNumber = ?"
        self.db.execute_query(query, (amount, account_number))
        self.log_transaction(account_number, "Deposit", amount)
        return self.get_account_balance(account_number)

    def withdraw(self, account_number, amount):
        balance = self.get_account_balance(account_number)
        if balance is None:
            raise ValueError("Account not found")
        if balance >= amount:
            query = "UPDATE Accounts SET Balance = Balance - ? WHERE AccountNumber = ?"
            self.db.execute_query(query, (amount, account_number))
            self.log_transaction(account_number, "Withdraw", amount)
            return self.get_account_balance(account_number)
        else:
            raise ValueError("Insufficient funds")

    def transfer(self, from_account_number, to_account_number, amount):
        self.withdraw(from_account_number, amount)
        self.deposit(to_account_number, amount)

    def get_account_details(self, account_number):
        query = "SELECT * FROM Accounts WHERE AccountNumber = ?"
        return self.db.fetchone(query, (account_number,))

    def get_transactions(self, account_number, from_date, to_date):
        query = """
            SELECT * FROM Transactions
            WHERE AccountNumber = ? AND DateTime BETWEEN ? AND ?
        """
        return self.db.fetchall(query, (account_number, from_date, to_date))

    def log_transaction(self, account_number, transaction_type, amount):
        query = """
            INSERT INTO Transactions (AccountNumber, Description, DateTime, TransactionType, TransactionAmount)
            VALUES (?, ?, ?, ?, ?)
        """
        description = f"{transaction_type} of {amount}"
        date_time = datetime.datetime.now()
        self.db.execute_query(query, (account_number, description, date_time, transaction_type, amount))