# While and For

num = int(input("Enter the number for which you need table: "))
i=1
while i<=10:
    print(i*num)
    i+=1


# While loop with else
num=int(input("Enter the number: "))
x=0
while x<num:
    print(x+1)
    x+=1
else:
    print("Limit crossed")



#### FOR LOOPS

for i in range(1,11):
    print(i)

print()
for i in [1,2,True,"Hello",9.7]:
    print(i)

print()
for i in range(1,11,2):
    print(i)

print()
for i in range(10,0,-1):
    print(i)

print()
for i in "Delhi":
    print(i)



