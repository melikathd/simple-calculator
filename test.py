def Addition():
    result = number + number_2
    print(result)


def Subtraction():
    result1 = number_2 - number
    print(result1)


def Multiplication():
    result3 = number_2 * number
    print(result3)


def Division():
    result4 = number_2 / number
    print(result4)


number = int(input("Enter first Number:"))
number_2 = int(input("Enter secound Number:"))

choice = input("choice an option  (+, -, *, /):")
if choice == "+":
    Addition()
elif choice == " - ":
    Subtraction()
elif choice == "*":
    Multiplication()
elif choice == "/":
    Division()
else:
    print("invalid choice")
