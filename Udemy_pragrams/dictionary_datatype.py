#A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)

# print(thisdict["brand"])

for x in thisdict:
    print(x)

print(len(thisdict))

thisdict["color"] = "red"
print(thisdict)