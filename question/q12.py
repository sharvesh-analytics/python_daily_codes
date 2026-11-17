a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if a>=b and a>=c:
    print("the largest value is a: ")

elif b>=a and b>=c:
    print("the largest value is b: ")

else:
    print("the largest value is c: ")