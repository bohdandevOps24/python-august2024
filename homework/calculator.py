# Ask the user to input two numbers
numberOne = int(input("Please provide first number: "))
numberTwo = int(input("Please provede second number: "))

# Perform the operations

addition = numberOne + numberTwo
subtraction = numberOne - numberTwo
multiplication = numberOne * numberTwo
division = numberOne / numberTwo

# Print the results in a user-friendly format

print(f"Addition: {numberOne} + {numberTwo} = {addition}")
print(f"Subtraction: {numberOne} - {numberTwo} = {subtraction}")
print(f"Multiplication: {numberOne} * {numberTwo} = {multiplication}")
print(f"Division: {numberOne} / {numberTwo} = {division}")