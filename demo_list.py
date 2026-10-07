my_list = [1,2,3,8,99,5,-2,8,1,0]
print(my_list[4])
print(my_list[-1])
total = 0
for value in my_list: # By value
    total += value
print(total)

total=0
for i in range(len(my_list)): # By index
    total += my_list[i]
print(total)

my_list[4] = 100 # Update
print(my_list)
my_list.append(999) # Add
print(my_list)
my_list.remove(999)
print(my_list)
my_list.remove(8)
print(my_list) # Remove CRUD Create Request Update Delete
