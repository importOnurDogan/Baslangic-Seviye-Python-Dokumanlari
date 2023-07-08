#   Hesap makinasi

num1=float(input("Enter first number:\t"))
ope=input("Enter operator:\t")
num2=float(input("Enter second number:\t"))
def Calc(op):
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print(num1 / num2)
ope2=ope
print(Calc(ope2))
