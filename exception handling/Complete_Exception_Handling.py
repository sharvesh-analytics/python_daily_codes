try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Please enter only numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result:", result)

finally:
    print("Thank you!")