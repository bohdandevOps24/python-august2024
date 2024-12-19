# Ask the user to input  number
inputNumber = int(input("Please provide number: "))

intConv = int(inputNumber)
floatConv = float(inputNumber)
stringConv = str(inputNumber)

print(f"Interger: {intConv} {type(intConv)}")
print(f"Float: {floatConv} {type(floatConv)}")
print(f"String: {stringConv} {type(stringConv)}")