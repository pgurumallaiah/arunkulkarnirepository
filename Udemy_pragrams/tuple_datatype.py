#tuple maintains index
#it allow dulicates
#it is immutable that means you can't change the value
#you can insert and delete the elements
#it maintains the insertion order
#its denoted by ()



tuple1=(12,32,42,"Python",-12,True)
print(tuple1)

print(type(tuple1))
print(list(tuple1))
tuple2=23,42,42,42
print(tuple2)

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])

list1=[12,323,43,53,"dwew"]

print(type(list1))

# to convert list to a tuple

print(tuple(list1))
tup1=tuple(list1)
print(tup1)

tup2=(12,3,43,53,"mental")
tup3=(544,553,65,95)
print(tup2+tup3)
print(tup2[1])
print(tup3*2)
print(tup2[1:])

print(tup2[1:4])
print(3 in tup2)
print(23 in tup2)
print(23 not in tup2)

print(len(tup2))

print(min(tup3))
print(max(tup3))














