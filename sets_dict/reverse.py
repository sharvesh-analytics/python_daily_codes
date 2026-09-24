data = {'a': 1, 'b': 2, 'c': 3}

reverse = {}

for key, value in data.items():

    reverse[value] = key

print(reverse)