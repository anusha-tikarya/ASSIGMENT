from dao.BankServiceProviderImpl import BankServiceProviderImpl
from entity.customer import Customer
class BankApp:
    def __init__(self, branch_name, branch_address):
        self.bank_service = BankServiceProviderImpl(branch_name, branch_address)

    def main(self):
        while True:
            print("\nMenu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Get Transactions")
            print("9. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.get_balance()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                self.list_accounts()
            elif choice == "8":
                self.get_transactions()
            elif choice == "9":
                break

    def create_account(self):
        customer_id = int(input("Enter Customer ID: "))
        name = input("Enter Customer Name: ")
        address = input("Enter Customer Address: ")
        customer = Customer(customer_id, name, address)

        acc_type = input("Enter Account Type (Savings, Current, ZeroBalance): ")
        balance = float(input("Enter Initial Balance: "))
        account_number = self.bank_service.create_account(customer, acc_type, balance)
        print(f"Account created successfully: {account_number}")

    def deposit(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount to Deposit: "))
        new_balance = self.bank_service.deposit(account_number, amount)
        print(f"Deposit successful. New Balance: {new_balance}")

    def withdraw(self):
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount to Withdraw: "))
        new_balance = self.bank_service.withdraw(account_number, amount)
        print(f"Withdrawal successful. New Balance: {new_balance}")

    def get_balance(self):
        account_number = int(input("Enter Account Number: "))
        balance = self.bank_service.get_account_balance(account_number)
        print(f"Current Balance: {balance}")

    def transfer(self):
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Amount to Transfer: "))
        self.bank_service.transfer(from_account_number, to_account_number, amount)
        print("Transfer successful.")

    def get_account_details(self):
        account_number = int(input("Enter Account Number: "))
        account = self.bank_service.get_account_details(account_number)
        print(f"Account Details: {account}")

    def list_accounts(self):
        accounts = self.bank_service.list_accounts()
        for account in accounts:
            print(account)

    def get_transactions(self):
        account_number = int(input("Enter Account Number: "))
        from_date = input("Enter From Date (YYYY-MM-DD): ")
        to_date = input("Enter To Date (YYYY-MM-DD): ")
        transactions = self.bank_service.get_transactions(account_number, from_date, to_date)
        for txn in transactions:
            print(txn)

if __name__ == "__main__":
    app = BankApp("Main Branch", "Indore")
    app.main()