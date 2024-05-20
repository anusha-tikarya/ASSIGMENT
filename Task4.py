print("Task 4 :")
accounts = {}
num_customers = int(input("Enter the number of customers: "))

for number in range(1, num_customers + 1):
    print(f"Enter details for Customer {number} ")
    account_number = int(input("Enter your account number: "))
    # Checking if customer has already entered account number or not
    if account_number not in accounts:
        balance = int(input("Enter your balance: "))
        accounts[account_number] = balance
    while True:
        account_number = int(input("Enter your account number for validation: "))
        if account_number in accounts:
            break
        else:
            print("Warning! Wrong credentials! Try again")
    print(f"Your account balance is ₹{accounts[account_number]}")
    