try:
    with open("student.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("The file does not exist.")