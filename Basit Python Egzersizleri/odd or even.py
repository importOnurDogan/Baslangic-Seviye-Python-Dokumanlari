#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

sayi=int(input("bir sayı giriniz :\t"))
if(sayi%4==0):
    print("bu sayı 4 ün katıdır.")
elif(sayi%2==0):
    print("bu bir çift sayıdır.")
else:
    print("bu bir tek sayıdır.")
print("\n")
    #---#

check=int(input("bölünecek sayıyı giriniz :\t"))
num=int(input("bölecek sayıyı giriniz :\t"))
if(check%num==0):
    print("bu sayılar birbirlerine tam bölünüyor.")
else:
    print("bu sayılar birbirlerine tam bölünemiyor.")

    #----# OLMASI GEREKEN

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
