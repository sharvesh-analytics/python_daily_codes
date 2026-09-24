data = {
    'x': {'a': {'i': 2, 'j': 3}},
    'y': {'b': {'i': 4, 'j': 5}}
}

total = 0

for outer in data.values():
    for inner in outer.values():
        for value in inner.values():
            total += value

print("Total:", total)