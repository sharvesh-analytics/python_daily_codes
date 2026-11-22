num = int(input("Enter number of term: "))

a=0
b=1
i=1

for i in range(num):
    print(a,end=" ")

    c=a+b
    a=b
    b=c
    i=i+1