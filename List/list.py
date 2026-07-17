   # LIST

# List ek ordered collection hai.

# 1.Multiple values store kar sakte hain.
# 2.Duplicate values allow hoti hain.
# 3.Data change kar sakte ho (Mutable).
# 4.Different data types store kar sakte ho.


# Create List

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)

# 1.Indexing

fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])

# 2.Change Value

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Grapes"

print(fruits)


# 3.Add Item

fruits = ["Apple", "Banana"]

fruits.append("Orange")

print(fruits)



# 4.Insert

fruits.insert(1, "Mango")

print(fruits)


# 5.Extend

list1 = [1,2]
list2 = [3,4]

list1.extend(list2)

print(list1)



# 6.Remove

fruits.remove("Banana")



# 7.loop 

for fruit in fruits:
    print(fruit)


# 8.sort 

numbers = [8,3,6,1]

numbers.sort()

print(numbers)



# 9. pop 

fruits.pop()


# 10.Lenght 

print(len(fruits))