print("Task: 10")
from abc import ABC, abstractmethod

# Task 7: Customer and Account Classes
class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone = phone
        self.__address = address

    # Getters and setters
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def print_customer_info(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"First Name: {self.__first_name}")
        print(f"Last Name: {self.__last_name}")
        print(f"Email: {self.__email}")
        print(f"Phone: {self.__phone}")
        print(f"Address: {self.__address}")


class Account:
    def __init__(self, account_number=None, account_type=None, balance=0.0):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__balance = balance

    # Getters and setters
    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_type(self):
        return self.__account_type

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.__account_type}")
        print(f"Account Balance: {self.__balance}")

    # Deposit and Withdraw methods
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}.")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        interest_rate = 0.045
        interest = self.__balance * interest_rate
        print(f"Interest calculated: {interest}")
        return interest


# Task 8: Inheritance and Polymorphism
class SavingsAccount(Account):
    def __init__(self, account_number=None, balance=0.0, interest_rate=0.045):
        super().__init__(account_number, "Savings", balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} added to balance.")


class CurrentAccount(Account):
    overdraft_limit = 500.0

    def __init__(self, account_number=None, balance=0.0):
        super().__init__(account_number, "Current", balance)

    def withdraw(self, amount):
        if self.get_balance() + CurrentAccount.overdraft_limit >= amount:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}. New balance is {self.get_balance()}.")
        else:
            print("Overdraft limit exceeded.")


# Task 9: Abstract Base Class
class BankAccount(ABC):
    def __init__(self, account_number=None, customer_name=None, balance=0.0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance

    # Getters and setters
    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_customer_name(self):
        return self.__customer_name

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Customer Name: {self.__customer_name}")
        print(f"Balance: {self.__balance}")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccountV2(BankAccount):
    def __init__(self, account_number=None, customer_name=None, balance=0.0, interest_rate=0.045):
        super().__init__(account_number, customer_name, balance)
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)
        print(f"Deposited {amount}. New balance is {self.get_balance()}.")

    def withdraw(self, amount):
        if self.get_balance() >= amount:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}. New balance is {self.get_balance()}.")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} added to balance.")


class CurrentAccountV2(BankAccount):
    overdraft_limit = 500.0

    def __init__(self, account_number=None, customer_name=None, balance=0.0):
        super().__init__(account_number, customer_name, balance)

    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)
        print(f"Deposited {amount}. New balance is {self.get_balance()}.")

    def withdraw(self, amount):
        if self.get_balance() + CurrentAccountV2.overdraft_limit >= amount:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}. New balance is {self.get_balance()}.")
        else:
            print("Overdraft limit exceeded.")

    def calculate_interest(self):
        print("Current accounts do not accrue interest.")


# Task 10: Has A Relation / Association
class Bank:
    def __init__(self):
        self.accounts = []
        self.next_account_number = 1001

    def create_account(self, customer, account_type, balance):
        account_number = self.next_account_number
        self.next_account_number += 1

        if account_type.lower() == "savings":
            account = SavingsAccountV2(account_number, customer.get_first_name(), balance)
        elif account_type.lower() == "current":
            account = CurrentAccountV2(account_number, customer.get_first_name(), balance)
        else:
            print("Invalid account type.")
            return None

        self.accounts.append(account)
        return account

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def get_account_balance(self, account_number):
        account = self.get_account_by_number(account_number)
        if account:
            return account.get_balance()
        else:
            print("Account not found.")
            return None

    def deposit(self, account_number, amount):
        account = self.get_account_by_number(account_number)
        if account:
            account.deposit(amount)
            return account.get_balance()
        else:
            print("Account not found.")
            return None

    def withdraw(self, account_number, amount):
        account = self.get_account_by_number(account_number)
        if account:
            account.withdraw(amount)
            return account.get_balance()
        else:
            print("Account not found.")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account_by_number(from_account_number)
        to_account = self.get_account_by_number(to_account_number)
        if from_account and to_account:
            if from_account.get_balance() + (CurrentAccountV2.overdraft_limit if isinstance(from_account, CurrentAccountV2) else 0) >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred {amount} from Account {from_account_number} to Account {to_account_number}.")
                return True
            else:
                print("Insufficient funds for transfer.")
                return False
        else:
            print("One or both accounts not found.")
            return False

    def get_account_details(self, account_number):
        account = self.get_account_by_number(account_number)
       