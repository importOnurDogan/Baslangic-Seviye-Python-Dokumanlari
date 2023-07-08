#Write a function that takes an ordered list of numbers
#(a list where the elements are in order from smallest to largest) and another number.
#The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean

def fonksyon1(a):
    result = 0
    for i in list1:
        if(i==a):
            result+=1
        else:
            continue
    if (result>0):
        print(True)
    else:
        print(False)

list1=[3,4,5,77,6]
num1=int(input("sayı giriniz :\t"))
fonksyon1(num1)
