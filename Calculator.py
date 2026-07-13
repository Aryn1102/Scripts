'''try:
    a=float(input("Enter first no.: "))
    b=float(input("Enter second no.: "))
    operator=input("Enter operator (+,-,*,/): ")
    if operator in ["+", "-", "*", "/"]:
        if operator == "+":
            print(f"{a} + {b} = {a+b}")
        elif operator == "-":
            print(f"{a} - {b} = {a-b}")
        elif operator == "*":
            print(f"{a} * {b} = {a*b}")
        elif operator == "/":
            if b != 0:
                print(f"{a} / {b} = {a/b}")
            else:
                print("Error: Division by zero")
except ValueError:
    print("Invalid input")
'''

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b != 0:
        return a/b
    else:
        return "Error: Division by zero"

def main():
    try:
        a=float(input("Enter first no.: "))
        b=float(input("Enter second no.: "))
        operator=input("Enter operator (+,-,*,/): ")
        if operator in ["+", "-", "*", "/"]:
            if operator =="+":
                print(f"{a} + {b} = {add(a, b)}")
            elif operator =="-":
                print(f"{a} - {b} = {subtract(a, b)}")
            elif operator =="*":
                print(f"{a} * {b} = {multiply(a, b)}")
            elif operator =="/":
                result = divide(a, b)
                if result == "Error: Division by zero":
                    print(result)
                else:
                    print(f"{a} / {b} = {result}")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
    