number = int(input("Enter a number to see its multiplication table:"))

for i in range(1, 11):  # Loop from 1 to 10
    product = number * i  # Calculate the product
    print(f"{number} * {i} = {product}")
