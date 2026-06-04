###### Higher Order Functions ######
# continuation of lambdafunction.py file

def sq(x):
    return x**2

# transform is an higher order function
def transform(f,L):
    output = []
    for i in L:
        output.append(f(i))
    return (output)

print(transform(sq,[3,2,1,4,23,321]))

l = [1,2,3,4,5,6,7,8,9]
print(transform(lambda x: x**2, l))
print(transform(lambda x: x**3, l))




####### Other higherorder function ####### - MAP, FILTER, REDUCE

### MAP ###
## expects a lambda function and a list

#1. square of a list
x = map(lambda x:x**2, [1,2,3,4,5])
print(list(x))

#2. odd/even labelling of a list
x = map(lambda x: 'even' if x%2==0 else 'odd', [1,2,3,4,5,6,7,8])
print(list(x))

#3. extract all names from the dict
usersss = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]
# for i in users:
#     print(i['name'])

print(list(map(lambda users: users['name'], usersss)))
print(list(map(lambda users: users['age'], usersss)))
print(list(map(lambda users: users['gender'], usersss)))




### FILTER ###
# Filters the list based on condition
# lambda function and a list


# filters number less than 5
l = [1,2,3,4,5,6,7,8,9,0,10]
print(list(filter(lambda x: x>5, l)))

# fruits starting with 'a' or 'b'
fruits = ['apple','guava','cheery','berry','amla']
print(list(filter(lambda fruit: fruit.startswith('a') or fruit.startswith('b'), fruits)))





##### REDUCE #####
# present in functools module
# lambda function, list

# add numbers in the list
import functools as ft
print(ft.reduce(lambda x,y : x+y, [1,2,3,4,5,6,7,8,9])) ## lambda can have only 2 argument in reduce

#find minimum
print(ft.reduce(lambda x,y: x if x<y else y, [0,4,32,4,5,3,23,90,32,43,4,32]))

#find maximum
print(ft.reduce(lambda x,y: x if x>y else y, [3,4,32,4,5,3,23,90,32,43,4,32]))