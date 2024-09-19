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

total_monthly_payment = float_input("Enter your monthly payment amount: ", default=my_monthly_payment)

total_interest_paid = 0
remaining_loans = num_loans
months = 0

while remaining_loans > 0:
    months += 1
    total_paid_this_month = 0

    #Distribute total monthly payment equally among remaining loans
    remaining_loan_indices = [i for i, loan in enumerate(loans) if loan["principal"] > 0]
    monthly_payment_per_loan = total_monthly_payment / len(remaining_loan_indices)

    for i in remaining_loan_indices:
        loan = loans[i]
        
        monthly_interest_rate = loan["annual_interest_rate"] / 100 / 12
        interest = loan["principal"] * monthly_interest_rate
        principal_payment = monthly_payment_per_loan - interest

        if principal_payment <= 0:
            print("Warning: Monthly payment is too low to cover the interest!")
            break

        if principal_payment > loan["principal"]: #Makes it so it doesn't say total payment is more than it should be if your monthly payment is more than the outstanding balance in the final month
            principal_payment = loan["principal"]

        loan["principal"] -= principal_payment
        total_interest_paid += interest
        total_paid_this_month += (principal_payment + interest)

        if loan["principal"] <= 0:
            remaining_loans -= 1

total_amount_spent = total_monthly_payment * months

print(f'\nPaying off this debt will take {months} months and will cost ${total_amount_spent:,.2f} in total, with ${total_interest_paid:,.2f} of that being interest.')
input("\nPress Enter to exit...")
