print("TASK 1:")
credit_score = int(input("Please enter your credit score: "))
annual_income = int(input("Please enter your annual income: "))

if credit_score > 700 and annual_income > 50_000:
    print("Congrats you are eligible for loan!!")
else:
    print("We're sorry you are not eligible for the loan!!")