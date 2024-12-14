mi = input("Enter your monthly income:")
me = input("ENter your total monthly expenses:") 
ms = mi - me
projectedSavings = ms * 12 + (ms * 12 * 0.5)
print("Your monthly savings are", mi - me)
print("Projected savings after one year, with interest, is:", (projectedSavings))

