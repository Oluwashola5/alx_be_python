num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
# operation = str(input("Choose the operation (+, -, *, /):"))

# match operation:
#     case "+":
#         print ("The result is", (num1 + num2))
#     case "-":
#         print ("The result is", (num1 - num2))
#     case "*":
#         print ("The result is", (num1 * num2))
#     case "/":
#         print ("The result is", (num1 / num2))
#     case _:
#         print ("Invalid operator entered")


# Ask the user to choose an operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")

        
# day = input("Enter a day of the week (Monday-Sunday): ").lower()

# match day:
#     case "monday":
#         print("Ugh, Mondays...")
#     case "tuesday":
#         print("Just another workday...")
#     case "wednesday":
#         print("Hump day!")
#     case "thursday":
#         print("Almost there...")
#     case "friday":
#         print("TGIF!")
#     case "saturday" | "sunday":  # Match multiple values with pipe (|)
#         print("Weekend vibes!")
#     case _:
#         print("Invalid day entered.")
