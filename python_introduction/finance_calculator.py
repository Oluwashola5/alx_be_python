monthly_income = input("Enter your monthly income:")
montly_expenses = input("ENter your total monthly expenses:") 
monthly_savings = monthly_income - monthly_expenses
projectedSavings = monthly_savings * 12 + (monthly_savings * 12 * 0.5)
print("Your monthly savings are", (monthly_savings))
print("Projected savings after one year, with interest, is:", (projectedSavings))

