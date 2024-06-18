# Initialize variables for monthly income and expenses
monthly_income = 500
rent = 150
groceries = 60
utilities = 20
transportation = 30
entertainment = 400

# Calculate total monthly expenses
total_expenses = rent + groceries + utilities + transportation + entertainment
print("Total monthly expenses:", total_expenses)

# Calculate remaining balance after expenses
remaining_balance = monthly_income - total_expenses
print("Remaining balance:", remaining_balance)

# Initialize savings_amount to a default value
savings_amount = 0

# Determine savings action based on remaining balance
if remaining_balance >= 0:
    savings_amount = remaining_balance * 0.5
    print("Saving 50% of the remaining balance:", savings_amount)
else:
    print("Warning: Remaining balance is negative. Unable to save.")

# Print the final savings amount
print("Final savings amount:", savings_amount)