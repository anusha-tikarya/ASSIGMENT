print("Task 6:")
transactions = []
while True:
    
    choice = int(input("""Enter your choice:
1. Deposit
2. Withdraw
3. Exit
"""))
    if choice == 1:
        deposit_amount = int(input("Enter deposit amount: "))
        transactions.append({'Transaction Type': 'Deposit', 'Amount': deposit_amount})

    elif choice == 2:
        withdrawal_amount = int(input("Enter withdrawal amount: "))
        transactions.append({'Transaction Type': 'Withdraw', 'Amount': withdrawal_amount})

    elif choice == 3:
        break

print(transactions)