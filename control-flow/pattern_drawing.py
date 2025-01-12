size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to print each row
while row < size:
    # Use for loop to print asterisks on the same line
    for col in range(size):
        print("*", end="")  # Print '*' without moving to the next line
    print()  # Move to the next line after printing all asterisks in the row
    row += 1  # Increment the row counter





# while age < 18:
#   age = int(input("Enter your age (must be 18 or older): "))

# print("You are old enough to proceed.")

# secret_number = 7

# guess_count = 0
# guess = 0

# while guess != secret_number:
#   guess_count += 1
#   guess = int(input("Guess a number between 1 and 10: "))

# print(f"You guessed it in {guess_count} tries!")