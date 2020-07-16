#list maintains index
#it allow dulicates
#it is mutable that means you can change the value
#you can insert and delete the elements
#it maintains the insertion order
#its denoted by []


#list is mutable

list1=[1,2,"Hello","Apple","orange","Banana"]
list2="Python"
print(list1)
list1.append(10)
print(list1)
print(list1.insert(0,450))
print(list1)
print(list2)

print(list1[0])
print(list1[2:])
print(list1*2)
list1[0]='20'
print(list1)


#list operator
#concatenation


demo1=[10,20,30,"Pineappale"]
demo2=[100,200,300,400]
print(demo1+demo2)

# repetition

print(demo1*2)

# slicing
print(demo2[2:])

print(demo1[:2])

print(10 in demo1)
print(123 in demo1)

print(10 not in demo1)
print(len(demo1))


print(max(demo2))
print(min(demo2))

# add the item to the end of the list

print(demo2.append(500))
print(demo2)


print(demo2.insert(2,"Java"))
print(demo2)

print(demo2.remove(200))


demo3=[10,20,30]
print(len(demo3))

demo3.reverse()
print(demo3)

demo4=[12,32,54,65,655,65654,343]
# for ascending order
demo4.sort()
print(demo4)


#for descending order
demo4.sort(reverse=True)
print(demo4)


# we can convert tuple to a list

tuple1=('helo',10,34)
print(list(tuple1))

list4=[10,23,43,53]
print(tuple(list4))

list6=[10,10,23,434,343,33,33]
print(list6)


list7=[12,-3,43,-53,535,6,-63]
print(list7)


#removing the elements

print(list7.remove(12))
print(list7)

# delete based on the index
del(list7[1])
print(list7)

# to remove the last  element of the list
print(list7.pop())
print(list7)









# for x in list1:
#     print(x)


list4=[10,23,43,53]



