from abc import ABC, abstractmethod
import re

# Task 7: Class & Object

class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    # Getter and Setter methods
    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.email = email
        else:
            raise ValueError("Invalid email address")

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        if re.match(r"^\d{10}$", phone):
            self.phone = phone
        else:
            raise ValueError("Invalid phone number")

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def print_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email Address: {self.email}")
        print(f"Phone Number: {self.phone}")
        print(f"Address: {self.address}")

class Account(ABC):
    last_acc_no = 1000

    def __init__(self, account_type=None, balance=0.0, customer=None):
        Account.last_acc_no += 1
        self.account_number = Account.last_acc_no
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    def get_account_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def print_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: {self.balance}")
        print("Customer Information:")
        self.customer.print_info()

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, balance=0.0, customer=None, interest_rate=4.5):
        super().__init__('Savings', balance, customer)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Calculated interest: {interest}. New Balance: {self.balance}")

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 5000

    def __init__(self, balance=0.0, customer=None):
        super().__init__('Current', balance, customer)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance + CurrentAccount.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")

    def calculate_interest(self):
        print("Current accounts do not accrue interest")

# Task 9: Abstraction

class BankAccount(ABC):
    def __init__(self, account_number=None, customer_name=None, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccountBA(BankAccount):
    def __init__(self, account_number=None, customer_name=None, balance=0.0, interest_rate=4.5):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Calculated interest: {interest}. New Balance: {self.balance}")

class CurrentAccountBA(BankAccount):
    OVERDRAFT_LIMIT = 5000

    def __init__(self, account_number=None, customer_name=None, balance=0.0):
        super().__init__(account_number, customer_name, balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance + CurrentAccountBA.OVERDRAFT_LIMIT >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")

    def calculate_interest(self):
        print("Current accounts do not accrue interest")

# Task 10 & 11: Has A Relation / Association and Interface/Abstract class

class ICustomerServiceProvider(ABC):
    @abstractmethod
    def get_account_balance(self, account_number):
        pass

    @abstractmethod
    def deposit(self, account_number, amount):
        pass

    @abstractmethod
    def withdraw(self, account_number, amount):
        pass

    @abstractmethod
    def transfer(self, from_account_number, to_account_number, amount):
        pass

    @abstractmethod
    def get_account_details(self, account_number):
        pass

class IBankServiceProvider(ABC):
    @abstractmethod
    def create_account(self, customer, account_type, balance):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.get_balance()
        else:
            print("Account not found")
            return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            return account.get_balance()
        else:
            print("Account not found")
            return None

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            return account.get_balance()
        else:
            print("Account not found")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred {amount} from {from_account_number} to {to_account_number}")
            else:
                print("Insufficient balance for transfer")
        else:
            print("One or both accounts not found")

    def get_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.print_info()
        else:
            print("Account not found")

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name, branch_address):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer, account_type, balance):
        if account_type == 'Savings':
            account = SavingsAccount(balance, customer)
        elif account_type == 'Current':
            account = CurrentAccount(balance, customer)
        else:
            print("Invalid account type")
            return
        self.accounts[account.get_account_number()] = account
        print(f"Created {account_type} account with number: {account.get_account_number()}")

    def list_accounts(self):
        for account_number, account in self.accounts.items():
            account.print_info()

    def calculate_interest(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.calculate_interest()

class BankApp:
    def __init__(self):
        self.bank_service = BankServiceProviderImpl("Main Branch", "123 Bank Street")

    def run(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Calculate Interest")
            print("9. Exit")
            choice = input("Enter your choice: ")
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
                self.calculate_interest()
            elif choice == "9":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        print("Creating Account")
        customer = self.create_customer()
        account_type = input("Enter account type (Savings/Current): ")
        balance = float(input("Enter initial balance: "))
        self.bank_service.create_account(customer, account_type, balance)

    def create_customer(self):
        customer_id = input("Enter Customer ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email Address: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        return Customer(customer_id, first_name, last_name, email, phone, address)

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        self.bank_service.deposit(account_number, amount)

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        self.bank_service.withdraw(account_number, amount)

    def get_balance(self):
        account_number = int(input("Enter account number: "))
        balance = self.bank_service.get_account_balance(account_number)
        if balance is not None:
            print(f"Current balance: {balance}")

    def transfer(self):
        from_account_number = int(input("Enter from account number: "))
        to_account_number = int(input("Enter to account number: "))
        amount = float(input("Enter transfer amount: "))
        self.bank_service.transfer(from_account_number, to_account_number, amount)

    def get_account_details(self):
        account_number = int(input("Enter account number: "))
        self.bank_service.get_account_details(account_number)

    def list_accounts(self):
        self.bank_service.list_accounts()

    def calculate_interest(self):
        self.bank_service.calculate_interest()

if __name__ == "__main__":
    app = BankApp()
    app.run()