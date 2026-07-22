age = int(input("Enter your age: "))

if age < 18:
    raise Exception("You are not eligible.")

print("You are eligible.")