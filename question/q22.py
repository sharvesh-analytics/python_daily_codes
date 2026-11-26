num = int(input("enter the number"))

count=0

if num==0:
    count=1

while num!=0:
    num=num//10
    count=count+1

print("total digit",count)        