#Implement a function that takes as input three variables, and returns the largest of the three.
#Do this without using the Python max() function!

num11=int(input("ilk sayıyı giriniz :\t"))
num22=int(input("ikinci sayıyı giriniz :\t"))
num33=int(input("üçüncü sayıyı giriniz :\t"))

def sayilar(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print("en büyük sayı :\t",num1)
    elif(num2>num1 and num2>num3):
        print("en büyük sayı :\t",num2)
    else:
        print("en büyük sayı :\t",num3)

numbers=num11,num22,num33
sayilar(*numbers)
