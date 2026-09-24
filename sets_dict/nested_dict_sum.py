data = {
    'a': {'x': 10, 'y': 20},
    'b': {'x': 5, 'y': 15}
}

total = 0

for outer in data.values():
    for value in outer.values():
        total += value

print("Total Sum:", total)