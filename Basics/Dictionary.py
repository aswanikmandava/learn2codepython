months = {"0": "Jan", "1": "Feb", "2": "March"}

# keys
print "Return type: ", type(months.keys())
print "Keys:", months.keys()

# values
print "Values:", months.values()

# items
print "Return type:", type(months.items()[0])
print "Items:", months.items()

# Iterate through items and print key and value
for key, value in months.items():
    print "Key:", key, "Value:", value

# Iterate through keys
for key in months.keys():
    print "Key:", key

# Iterate through values
for value in months.values():
    print "Value:", value
