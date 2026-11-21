num = int(input("Enter the number:"))

fact = 1
i = 1

if num<0:
    print("Factorial not possible")

else:
    while i <= num:
        fact = fact*1
        i = i+1
    print("Factorial =", fact)    

