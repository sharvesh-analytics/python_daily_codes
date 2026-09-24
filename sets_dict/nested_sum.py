data = {
    'p': {'a': 5, 'b': 10},
    'q': {'a': 3, 'b': 7}
}


# total = 0

# for outer in data.values():
#     for value in outer.values():
#         total += value

# print("Total:", total)

# ONLY KEY 'a' SUM
total = 0

for outer in data.values():
    total += outer['a']

print("Sum of 'a':", total)


