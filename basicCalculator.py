if __name__ == '__main__':

    number1 = float(input(" please enter first number: "))

    operator = input(" please enter operator: ")

    number2 = float(input("please enter second number:"))

    if operator == "+":
        print(number1+number2)
    elif operator == "-":
        print(number1-number2)
    elif operator == "*":
        print(number1*number2)
    elif operator == "/":
        print(number1/number2)
    else:
        print("Invalid operator.")