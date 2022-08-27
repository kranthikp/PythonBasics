"""
lists
# collection of data in [] square brackets
# can contain any/all data types in a single list
# can contain other collections (lists, dictionaries, tuples) as list items
# mutable (items can be added, removed, changed)
# maintain order (can use index to find an item)
"""

fruits = ["apples", "peaches", "pears", "apples"]
years = [3, "1198", 2.5, 98, "1995"]

print(fruits, years)

"""
#to append new values to existing list
fruits.append("oranges")
print(fruits)

#list extend method extend list with other list
fruits.extend(years)
print(fruits)

#to remove an item from list, exact item match is must
fruits.remove("oranges")
print(fruits)

#another way is using index
fruits.pop(0)
print(fruits)

# to remove last item use -ve index
fruits.pop(-1)
print(fruits)
"""
numbers =  [5,122,12,33,65]
numbers.sort()
print(numbers)

print("apples" in fruits)
print("apple" in fruits)

#get count of items in list
print(fruits.count("apples"))
print(fruits.count("apple"))

#get index of an item from list
print(fruits.index("peaches"))