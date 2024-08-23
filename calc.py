#Create a function calc which gets operator and two numbers and returns the calculation result.
def calc(a,b,c):
    if a == "+" or a == "add":
        return b + c
    elif a == "-" or a == "sub":
        return b - c
    elif a == "/" or a == "div":
        return b/c
    elif a == "*" or a =="mul":
        return b*c
    elif a == "^" or a =="pow":
        return b**c
    elif a == "%" or a =="mod":
        return b%c


def main():
    operator = input("What's the operator?: ")
    num1 = float(input("What's num1?: "))
    num2 = float(input("What's num2?: "))
    result = calc(operator,num1,num2)
    print(result)
    


main()