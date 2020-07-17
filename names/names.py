import time
from binary_search_tree import BSTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
start_tree_time = time.time()
name_tree = BSTree()
for name in names_2:
    name_tree.insert(name)

for name in names_1:
    if name_tree.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print (f"tree runtime: {end_time - start_tree_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_list_time = time.time()
duplicates = []

# We'll sort the names_2 list so we can do a binary search on it
names_1.sort()
names_2.sort()

idx_1 = 0
idx_2 = 0
while True:
    if names_1[idx_1] == names_2[idx_2]:
        duplicates.append(names_1[idx_1])
        idx_1 += 1
        idx_2 += 1
    elif names_1[idx_1] < names_2[idx_2]:
        if idx_1 < len(names_1) - 1:
            idx_1 += 1
        else:
            break
    else:
        if idx_2 < len(names_2) - 1:
            idx_2 += 1
        else:
            break

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"sorted list runtime: {end_time - start_list_time} seconds")

