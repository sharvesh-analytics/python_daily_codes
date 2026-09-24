name = input("Enter student name: ")

math = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
sql = int(input("Enter SQL marks: "))

age = int(input("Enter age: "))
attendance = float(input("Enter attendance percentage: "))

# Subject list
subjects = ["Math", "Python", "SQL"]

# 1. Arithmetic Operators
total = math + python + sql
average = total / 3
percentage = (total / 300) * 100

print("\n----- RESULT -----")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)

# 2. Comparison Operators
passed_math = math >= 40
passed_python = python >= 40
passed_sql = sql >= 40

print("\n----- SUBJECT RESULT -----")
print("Math Passed:", passed_math)
print("Python Passed:", passed_python)
print("SQL Passed:", passed_sql)

# 3. Logical Operators
eligible = (
    age >= 18
    and attendance >= 75
    and percentage >= 60
)

print("\nEligible:", eligible)

# 4. Assignment Operators
bonus = 5
percentage += bonus

print("Percentage after bonus:", percentage)

# 5. Membership Operators
print("\nMath in subjects:", "Math" in subjects)
print("Java not in subjects:", "Java" not in subjects)

# 6. Identity Operators
a = subjects
b = subjects
c = ["Math", "Python", "SQL"]

print("\na is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)

# 7. Floor Division and Modulus
number = 17

print("\nFloor Division:", number // 5)
print("Remainder:", number % 5)

# 8. Exponent
print("Power:", 2 ** 3)

# 9. Bitwise Operators
x = 5
y = 3

print("\n----- BITWISE -----")
print("AND:", x & y)
print("OR:", x | y)
print("XOR:", x ^ y)
print("NOT:", ~x)
print("Left Shift:", x << 1)
print("Right Shift:", x >> 1)