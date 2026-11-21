num = int(input("enter the number:"))

fact=1

if num<0:
    print("Factorial is not in negative")

else:
    for i in range(1, num+1):
        fact = fact*1

    print("Factorial =", fact)        