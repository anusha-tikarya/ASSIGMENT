print("Task 3 :")
num_customers = int(input("Enter the number of customers: "))
for number in range(1, num_customers+1):
    name = input("Enter your name: ")
    print(f"Enter data for {name}")
    initial_balance = int(input("Enter initial balance: "))
    annual_interest_rate = int(input("Enter annual interest rate: "))
    years = int(input("Enter the number of years: "))
    future_balance = round(initial_balance*(1 + annual_interest_rate/100)**years)
    print(f"""{name}, your balance after applying compound interest for {years} years is 
₹{future_balance}""")
