# Python Collections
# dictionaries, uses curly braces
from data import me

# get data from dictionaries
print(me["first_name"])

# modify values inside dictionary
me["color"] = "Gray"

# add new key values to dictionary
me["age"] = 57


# read a non existing key will cause a code crash
# print(me["title"])

# check if a key exists
if "title" in me:
    print(me["title"])

print(me["address"])

address = me["address"]
print(address["street"] + " " + str(address["number"] + " " + address["city"]))
