from datetime import datetime

class Transaction:
    def __init__(self, account, description, transaction_type, transaction_amount):
        self.account = account
        self.description = description
        self.date_time = datetime.now()
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount

    def __str__(self):
        return (f"Transaction[Account={self.account.account_number}, Description={self.description}, "
                f"DateTime={self.date_time}, Type={self.transaction_type}, Amount={self.transaction_amount}]")