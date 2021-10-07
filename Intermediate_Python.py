###  Question to find out

# Why Tuple is more faster than List?


##################################################### List: ordered,mutablem allows duplicate elements
myList = ["banana", "cherry", "apple","apple"]
print(myList)

myList2 = [5, True, "apple" ,"banana"] # List allow different datatypes
print(myList2[-1]) # Select reverse of element in array

if "banana" in myList:
    print("yes")
else:
    print("no")
    
item = myList.pop() #Get last element from array (Stack)
myList.remove("apple") #Remove only one match
myList.reverse() 
myList.clear()

testSort = [2,4,0,-2,3,6,-7]
print(sorted(testSort)) # Sorted elements in array

mylist = [1] * 10 # Create new list with 1 in 10 times Ex. [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5] # Select begin - end of the array elements Ex. [2, 3, 4, 5]
a = mylist[::2] # select begin to end with 2 steps

###### ************* Important
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org  #### Both are referd to the same bytes in the memory
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

list_cpy = list_org.copy() # 3 Ways to copy only data from one array to another
list_cpy = list(list_org)
list_cpy = list_org[:]

list_cpy.append("orange") 
print(list_cpy)
print(list_org)

mylist = [1,2,3,4,5,6,7,8,9]
b = [i*i for i in mylist] # Expression with for loop interating

print(mylist)
print(b)
print('"""""""""""""""""""""""""""""')

##################################################### Tuple: ordered, immutabele, allows duplicate elements
mytuple = "Max", 28, "Boston"
mytuple = tuple(["Max", 28, "Boston"])
print(type(mytuple))
print(mytuple)

item = mytuple[-1]
print(item)

# mytuple[0] = "test" ## Can't run because tuple is immutable
for x in mytuple:
    print(x)

if "Boston" in mytuple:
    print("Yes")
else:
    print("No")

my_tuple = ('a','p','p','l','e')
print(len(my_tuple))
print(my_tuple.count('p'))
print("index:" + str(my_tuple.index('l')))

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(mylist)
print(my_tuple2)

a = (1,2,3,4,5,6,7,8,9)
b = a[2:5]
print(b)

my_tuple = "Max", 28, "Boston"
name , age, city = my_tuple
print(f"{name} {age} {city}")

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple

print(i1) # First item
print(i3) # Last item
print(i2) # all of elements left between

import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)  ## Tuple is more faster than List 
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)) #0.062963041s
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)) #0.007387499999999991

##################################################### Dictionarnies

mdict = {'name': 'Max', "age": 28, "City": "New York"}
print(mdict)

mdict2 = dict(name="Mary", age=27, city="New York")
print(mdict2)
print(type(mdict2))

value = mdict["name"]
print(value)

mdict["email"] = "max@xyz.com"
print(mdict)
print(id(mdict["email"]))

mdict["email"] = "coolmax@xyz.com"
print(mdict)
print(id(mdict["email"]))

del mdict["name"]
print(mdict)

mdict.pop("age")
print(mdict)

mdict.popitem()
print(mdict)

if "City" in mdict:
    print(mdict["City"])
    print("Hey")

try:
    print(mdict["name"])
except:
    print("Error")
    
mdict = {'name': 'Max', "age": 28, "City": "New York"}
for key in mdict.keys():
    print(key)

for key in mdict.values():
    print(key)
    
for key, value in mdict.items():
    print(key, value)

mdict_cpy = mdict # Assign as a pointer in the same address in memory
print(mdict_cpy is mdict) 

# Merge Dictionaries
mdict = {"name":"Max", "age": 28, "email": "max@xyz.com"}
mdict2 = dict(name="Mary", age=27, city="Boston")

mdict.update(mdict2)
print(mdict)
 
mdict = {3:9 , 6:36, 9:81}
print(mdict) 

value = mdict[3]
print(value)
mytuple = (8, 7)
mdict = {mytuple: 15}
print(mdict)

##################################################### SETs
myset = {1, 2, 3}
print(myset)
print(type(myset))

myset = set("Hello")
print(type(myset))

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.discard("H")
print(myset)

print(myset.pop())
print(myset)

for x in myset:
    print(x)

if 2 in myset:
    print("YES")
    
# ----------------------------- 
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)
print(id(u))

u = odds.intersection(primes)
print(u)
print(id(u))

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

diff = setB.difference(setA)
print(diff)

diff = setB.symmetric_difference(setA) # Not in intersect of A & B
print(diff)

setA.update(setB) # Add new elements from setB without duplication
print(setA)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setA.intersection_update(setB)
print(setA)

setA = {1,2,3}
setB = {1,2,3,10,11,12}
print(setA.issubset(setB)) # is all elements on setA are in setB ?
print(setB.issubset(setA))

setC = {7,8}
print(setB.issuperset(setA))
print(setA.isdisjoint(setC))

setA = {1,2,3,4,5,6}
setB = setA.copy()
setB = set(setA)
print(id(setA))
print(id(setB))

print(setA)
print(setB)

# ----------------------------- 
a = frozenset([1,2,3,4])
# a.add(2)
print(type(a))
print(a)
