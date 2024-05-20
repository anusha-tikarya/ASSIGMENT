class Customer:
    def __init__(self, customer_id, first_name, last_name, email_address, phone_number, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
        self.__phone_number = phone_number
        self.__address = address
    
    # Getter methods
    def get_customer_id(self):
        return self.__customer_id
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_email_address(self):
        return self.__email_address
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_address(self):
        return self.__address
    
    # Setter Methods
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_address(self, address):
        self.__address = address

    def print_all_information(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"First Name: {self.__first_name}")
        print(f"Last Name: {self.__last_name}")
        print(f"Email Address: {self.__email_address}")
        print(f"Phone Number: {self.__phone_number}")
        print(f"Address: {self.__address}")

class Account:
    def __init__(self, acc_number, acc_type, acc_balance):
        self.__acc_number = acc_number
        self.__acc_type = acc_type
        self.__acc_balance = acc_balance

    # Getter Methods
    def get_acc_number(self):
        return self.__acc_number
    
    def get_acc_type(self):
        return self.__acc_type
    
    def get_acc_balance(self): 
        return self.__acc_balance

    # Setter Methods
    def set_acc_number(self, acc_number):
        self.__acc_number = acc_number

    def set_acc_type(self, acc_type):
        self.get_acc_type = acc_type

    def set_acc_balance(self, acc_balance):
        self.__acc_balance = acc_balance

    def print_all_information(self):
        print(f"Account Number: {self.__acc_number}")
        print(f"Account Type: {self.__acc_type}")
        print(f"Account Balance: ₹{self.__acc_balance}")

    def deposit(self, amount):
        self.__acc_balance += amount
        print(f"Deposit of ₹{amount} was successful")
        print(f"Updated Balance: ₹{self.__acc_balance}")

    def withdraw(self, amount):
        if amount > self.__acc_balance:
            print("Insufficient balance")
        else:
            self.__acc_balance -= amount
            print(f"Withdrawal of ₹{amount} was successful")
            print(f"Updated Balance: ₹{self.__acc_balance}")

    def cal_interest(self):
        if self.__acc_type.lower() == 'savings':
            interest = self.__acc_balance * 0.45
            self.__acc_balance += interest
            print("Interest Calculated Successfully")
            print(f"Interest = {interest}")
            print(f"Updated Balance: ₹{self.__acc_balance}")
        else:
            print("Interest calculation is only applicable for savings accounts.")
    
class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def create_customer(self, customer_id, first_name, last_name, email_address, phone_number, address):
        customer = Customer(customer_id, first_name, last_name, email_address, phone_number, address)
        self.customers.append(customer)
        return customer

    def create_account(self, acc_number, acc_type, acc_balance):
        account = Account(acc_number, acc_type, acc_balance)
        self.accounts.append(account)
        return account
    
    def perform_operations(self):
        account = self.create_account(1234, "Savings", 50000)
        account.print_all_information()
        account.deposit(500)
        account.withdraw(600)
        account.cal_interest()

if __name__ == "__main__":
    bank = Bank()
    bank.perform_operations()