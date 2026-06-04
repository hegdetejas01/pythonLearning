# sets and set theory

### Creating sets

s = {} # this doesn't create set, this creates a dictoinary
print(type(s))

s = set() # this creates a set
print(type(s))
print(s)

s = {1,2} # 1D set
print(s)

# s = {1,2,{3,4}} --> This throws error because set inside a set. Set is mutable and it cant be a element of set

s = {1,2.3,True,'hello'} 
print(s) # output = {1, 2.3, 'hello'}, since sets doesn't allow duplicates and true is considered as 1 in python, true is not printed

s = {1,2.3,'okay',(4,5.6)} # tuple is immutable and it can be element
print(s)

s = set([1,2,3])
print(s)
s = set((1,2,3))
print(s)

s1 = {1,2,3}
s2 = {2,1,3}
print(s1 == s2) # True - because tuple is unordered



### Accessing the elements - elements cant be accessed by indexing or slicing


### Editing the items - not allowed


### Adding/Updating items into set
s = {1,2,3,4}
s.add(5) # Position of the addition can't be controlled
print(s)

s.update([5,6,7]) #adds multiple items to the set
print(s)
s.update((8,9)) #adds multiple items to the set
print(s)
s.add((10,11)) # adds tuple (10,11)
print(s)
# s.add([1,2,3]) --> this throws error
# print(s)


### Deleting set
s = {12,32,32}
del s
# print(s) --> throws error
# can't delete a perticular element from the set through indexing


s = {1,2,3,4,5}
s.discard(5) # discards the particular element
print(s)
s.discard(10) # doesn't throw error

s = {1,2,3,4,5}
s.remove(5)
print(s)
# s.remove(10) ---> this throws error

s = {1,2,3,4,5}
s.pop() # it deletes an item randomly
print(s)

s = {1,2,3,4,5}
s.clear() # the list will get emptied
print(s)









############ OPERATIONS #############

## UNION operation( | )
s1 = {1,2,3,4,5}
s2 = {4,5,6,7}
print(s1 | s2)

## INTERSECTION ( & )
print(s1 & s2)

## DIFFERENCE ( - )
print(s1 - s2) # those in s1 which are not in s2
print(s2 - s1) # those in s2 which are not in s1

## SYMMETRIC DIFFERENCE ( ^ )
# prints everything except the commons
print(s1 ^ s2)

## membership operation
print(1 in s1)
print(6 not in s2)

## iteration
for i in s1:
    print(i)







############### FUNCTIONS ############

print(len(s1))
print(sum(s1))
print(min(s1))
print(max(s1))
print(sorted(s1, reverse=True)) ## Gives the result in List

print(s1.union(s2)) # s1 | s2

s1.update(s2) # s1 = s1 | s2
print(s1)
print(s2)
