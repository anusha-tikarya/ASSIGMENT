
from util.DBconn import DBConnection
from dao.IBankRepository import IBankRepository


class BankRepositoryImpl(IBankRepository, DBConnection):
    def __init__(self):
        super().__init__()

    def create_account(self, customer, accNo, accType, balance):
        query = """
            INSERT INTO accounts (account_number, account_type, balance, customer_id)
            VALUES (?, ?, ?, ?)
        """
        self.execute_query(query, (accNo, accType, balance, customer.customer_id))

    def list_accounts(self):
        query = "SELECT * FROM accounts"
        return self.fetchall(query)

    def calculate_interest(self):
        query = "UPDATE accounts SET balance = balance * 1.04 WHERE account_type = 'Savings'"
        self.execute_query(query)

    def get_account_balance(self, account_number):
        query = "SELECT balance FROM accounts WHERE account_number = ?"
        result = self.fetchone(query, (account_number,))
        return result[0] if result else None

    def deposit(self, account_number, amount):
        query = "UPDATE accounts SET balance = balance + ? WHERE account_number = ?"
        self.execute_query(query, (amount, account_number))
        return self.get_account_balance(account_number)

    def withdraw(self, account_number, amount):
        balance = self.get_account_balance(account_number)
        if balance is None:
            raise ValueError("Account not found")
        if balance >= amount:
            query = "UPDATE accounts SET balance = balance - ? WHERE account_number = ?"
            self.execute_query(query, (amount, account_number))
            return self.get_account_balance(account_number)
        else:
            raise ValueError("Insufficient funds")

    def transfer(self, from_account_number, to_account_number, amount):
        self.withdraw(from_account_number, amount)
        self.deposit(to_account_number, amount)

    def get_account_details(self, account_number):
        query = "SELECT * FROM accounts WHERE account_number = ?"
        return self.fetchone(query, (account_number,))

    def get_transactions(self, account_number, from_date, to_date):
        query = """
            SELECT * FROM transactions
            WHERE account_number = ? AND date_time BETWEEN ? AND ?
        """
        return self.fetchall(query, (account_number, from_date, to_date))