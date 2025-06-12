while True:

 print("Welcome to the calculator")
 num1 = int(input("Please enter the first number: "))
 num2 = int(input("Please enter the second number: "))
 print("Please select the operation you want to perform:")

 operation = input("Choose operation (+, -, *, /): ")

 if operation == "+":
    print("Result:", num1 + num2)

 elif operation == "-":
    print("Result:", num1 - num2)
 elif operation == "*":
    print("Result:", num1 * num2)
 elif operation == "/":
  if num2 != 0:
        print("Result:", num1 / num2)
 else:
        print("You cannot divide a number by zero!")