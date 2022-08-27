"""
dictionaries
#content: key/value parings
#mutable: can be changed
#order: maintain order of entry as of python 3.7
#syntax: curly braces contains keys and values
    keys and values are separated by a colon
"""
#example
"""
years = {"Kranthi":229, "Sagar":227, "panda":229, "mitta":227}
print(years)


#return values dict key passed
print(years.get("Sagar"))

#items() method returns dict entire in order
print(years.items())

#keys() method returns dict keys in order
print(years.keys())

#popitem() item method allows to remove last item from dict
print(years.popitem())

#setdefault() item method allows to set default values to key
print(years.setdefault("Kranthi"))
print(years)
print(years.setdefault("Kumar",22))
print(years)

"""

new_years = {"rocks":4, "arrows":18}
new_years.update(new_years)
print(new_years)

new_years.update(food=450)
print(new_years)

new_years.update(food=450, new=456)
print(new_years)