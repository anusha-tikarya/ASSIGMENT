print("Task :8")
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
        print(f"Balance: {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient balance")

    def calculate_interest(self):
        interest_rate = 0.045
        interest = self.__balance * interest_rate
        self.__balance += interest
        print(f"Interest calculated: {interest}. New Balance: {self.__balance}")


class SavingsAccount(Account):
    def __init__(self, account_number=None, balance=0.0, interest_rate=0.045):
        super().__init__(account_number, "Savings", balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.set_balance(self.get_balance() + interest)
        print(f"Interest calculated: {interest}. New Balance: {self.get_balance()}")


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 500.0

    def __init__(self, account_number=None, balance=0.0):
        super().__init__(account_number, "Current", balance)

    def withdraw(self, amount):
        if self.get_balance() + self.OVERDRAFT_LIMIT >= amount:
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrew: {amount}. New Balance: {self.get_balance()}")
        else:
            print("Insufficient balance, overdraft limit exceeded")


class Bank:
    def main(self):
        while True:
            print("1. Create Savings Account")
            print("2. Create Current Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Calculate Interest")
            print("6. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                account = SavingsAccount(account_number=123456789, balance=1000.0)
                print("Savings Account created.")
                account.print_account_info()
            elif choice == 2:
                account = CurrentAccount(account_number=987654321, balance=500.0)
                print("Current Account created.")
                account.print_account_info()
            elif choice == 3:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == 4:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == 5:
                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                else:
                    print("Interest calculation is not applicable for Current Account.")
            elif choice == 6:
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    bank = Bank()
    bank.main()