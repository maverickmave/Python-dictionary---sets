#dictionary
phonebook = {'Sam':'666-897','Carlisle':'666-765','Ryan':'666-098'}
#add
phonebook['David']='777-098'
print(phonebook)
#read
print(phonebook.get(('Carlisle')))
#get
print(phonebook.get('David'))
#update
phonebook.update({'Troy':'777-987'})
#remove
del phonebook['Carlisle']
print(phonebook)
#keys
print(phonebook.keys())
#values
print(phonebook.values())
#keys values pair method
print(phonebook.items())
#merge method
newphonebook={'Aron':'444-567','Trevor':'444-098'}
phonebook.update(newphonebook)
#clearmethod
phonebook.clear()
print(phonebook)


#sets
# creating a set
numbers = {1, 2, 3, 4, 5}
print("Original set:", numbers)

# add
numbers.add(6)
print("After add:", numbers)

# update
numbers.update({7, 8})
print("After update:", numbers)

# remove
numbers.remove(1)
print("After remove:", numbers)

# discard
numbers.discard(10)  # no error even if element is absent
print("After discard:", numbers)

# pop
popped = numbers.pop()
print("Popped element:", popped)
print("Set after pop:", numbers)

# clear
numbers.clear()
print("After clear:", numbers)

# create two sets for operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A:", set_a)
print("Set B:", set_b)

# union
print("Union:", set_a | set_b)
print("Union using union():", set_a.union(set_b))

# intersection
print("Intersection:", set_a & set_b)
print("Intersection using intersection():", set_a.intersection(set_b))

# difference
print("Difference:", set_a - set_b)
print("Difference using difference():", set_a.difference(set_b))

# symmetric difference
print("Symmetric difference:", set_a ^ set_b)
print("Symmetric difference using symmetric_difference():", set_a.symmetric_difference(set_b))

# subset, superset, disjoint
print("Is set_a subset of set_b?", set_a.issubset(set_b))
print("Is set_a superset of {1,2}?", set_a.issuperset({1, 2}))
print("Are sets disjoint?", set_a.isdisjoint({7, 8, 9}))

# copy
set_c = set_a.copy()
print("Copy of set A:", set_c)

# len
print("Length of set A:", len(set_a))

# membership
print("Is 3 in set A?", 3 in set_a)
