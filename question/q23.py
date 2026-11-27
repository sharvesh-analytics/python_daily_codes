
num = int(input("enter the number"))

sum = 0

num=abs(num)

while num>0:
    digit = num%10
    sum = sum + digit
    num = num//10

print("sums of digits:",sum)