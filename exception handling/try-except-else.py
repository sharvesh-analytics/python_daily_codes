try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result:", result)