my_loans = [
    {"principal": 5654.45, "annual_interest_rate": 2.75},
    {"principal": 6747.59, "annual_interest_rate": 3.7},
    {"principal": 7882.19, "annual_interest_rate": 4.99},
    {"principal": 7851.23, "annual_interest_rate": 5.5}
]
my_monthly_payment = 225.03

def float_input(prompt, default=None):
    while True:
        user_input = input(f"{prompt} (Default = {default}) ")
        if user_input == '' and default is not None:
            return default
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def int_input(prompt, default=None):
    while True:
        user_input = input(f"{prompt} (Default = {default}) ")
        if user_input == '' and default is not None:
            return default
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

num_loans = int_input("Enter the number of loans:", default=len(my_loans))

loans = []

for i in range(num_loans):
    print(f"\nLoan {i + 1}:")
    principal = float_input("Enter the principal amount: ", default=my_loans[i]["principal"] if i < len(my_loans) else None)
    annual_interest_rate = float_input("Enter the annual interest rate (as a percentage): ", default=my_loans[i]["annual_interest_rate"] if i < len(my_loans) else None)
    loans.append({"principal": principal, "annual_interest_rate": annual_interest_rate})

total_payment = float_input("Enter your monthly payment amount: ", default=my_monthly_payment)

total_interest_paid = 0

loan_data = []

for loan in loans:
    principal = loan["principal"]
    annual_interest_rate = loan["annual_interest_rate"]
    monthly_interest_rate = annual_interest_rate / 100 / 12
    remaining_balance = principal
    total_paid_for_loan = 0
    months = 0

    while remaining_balance > 0:
        interest = remaining_balance * monthly_interest_rate
        principal_payment = total_payment - interest
        
        if principal_payment <= 0:
            print("Warning: Monthly payment is too low to cover the interest!")
            break
        
        if principal_payment > remaining_balance: #Makes it so it doesn't say total payment is more than it should be if your monthly payment is more than the outstanding balance in the final month
            principal_payment = remaining_balance
        
        remaining_balance -= principal_payment
        total_paid_for_loan += (principal_payment + interest)
        months += 1

    total_interest_paid += (total_paid_for_loan - principal)
    
    loan_data.append({"principal": principal, "months": months, "total_paid_for_loan": total_paid_for_loan})

total_months = max(loan['months'] for loan in loan_data)
total_amount_spent = sum(loan['total_paid_for_loan'] for loan in loan_data)

print(f'\nPaying off this debt will take {total_months} months and will cost ${round(total_amount_spent, 2)} in total, with ${round(total_interest_paid, 2)} of that being interest.')

input("\nPress Enter to exit...")
