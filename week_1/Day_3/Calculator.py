# Pick an operation
# 1 add
# 2 sub
# 3 multi
# 4 Div
print("Pick an operation")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    # 1 adds
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("Answer:" + str(int(num1) + int(num2)))

elif operation == "2":
    # 2 sub
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("Answer:" + str(int(num1) - int(num2)))

elif operation == "3":
    # 3 multi
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("Answer:" + str(int(num1) * int(num2)))

elif operation == "4":
    # 4 div
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("Answer:" + str(int(num1) / int(num2)))

else:
    print("try again")
