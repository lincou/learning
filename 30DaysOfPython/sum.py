

input1 = input("Enter first number: ")
input2 = input("Enter second number: ") 
while num1 == type(int):
    try:
        num1 = int(input1)
    except ValueError:
        print("Please enter valid numbers")

while num2 == type(int):
    try:
        num2 = int(input2)
    except ValueError:
        print("Please enter valid numbers")

print(f"Sum of {input1} and {input2} is {num1+num2}")