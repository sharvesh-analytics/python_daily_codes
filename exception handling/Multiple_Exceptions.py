try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input. Please enter a number.")