# TO FIND TH SECOND LARGEST NO. 
nums = (10, 25, 5, 40, 30)

# Step 1: CONVERT TUPLES INTO LIST
lst = list(nums)

# Step 2: SORT
lst.sort()

# Step 3: SECOND LARGEST NO.
second_largest = lst[-2]

print("Second Largest:", second_largest)