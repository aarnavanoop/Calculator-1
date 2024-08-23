#Create a function calc which gets operator and two numbers and returns the calculation result.
def calc(a,b,c):
    if a == "+":
        return b + c
    elif a == "-":
        return b - c
    elif a == "/":
        return b/c
    elif a == "*":
        return b*c
    elif a == "^":
        return b**c
    elif a == "%":
        return b%c


def main():
    operator = input("What's the operator?: ")
    num1 = float(input("What's num1?: "))
    num2 = float(input("What's num2?: "))
    result = calc(operator,num1,num2)
    print(result)
    


main()