#set doesn't  maintains index
#it does'nt allow dulicates
#it is mutable that means you can change the value
#you can insert and delete the elements
#it doesn't maintains the insertion order or we cant the guarantee the order of the index
#its denoted by {}

# In Python, Set is an unordered collection of data type
# that is iterable, mutable and has no duplicate elements.
#A set is a collection which is unordered and unindexed.
#You cannot access items in a set by referring to an index,
# since sets are unordered the items has no index.


s1={1, "Bill", 75.50}
s2={1,1,1,34,"handle",754,894}



print(s1|s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

s1.add("Bill  gates")
print(s1)
s1.update(("manju","Preetham"))
print(s1)
s3=s1.remove("Bill")
print(s3)


set1={10,32,42,"tyiww"}
set1.add(37)
print(set1)


for x in s2:
    print(x)









