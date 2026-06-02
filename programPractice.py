# Get 2 int/float input from user and add them

print()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
add = num1 + num2
print(add)

# ORR
print(int(input("Enter First Num: ")) + int(input("Enter Second Num: ")))





# Get input from user, and add the digits

number = int(input("Enter a 3 digit number: "))
a = number%10
number //= 10
b = number%10
number //= 10
c = number
print("Sum is ", a+b+c)




# find the minimim of 3 numbers

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
minimum = min(num1,num2)
num3 = int(input("Enter number 3: "))
minimum = min(minimum, num3)
print(minimum)

# ORR
num1, num2, num3 = int(input("Enter number 1: ")), int(input("Enter number 2: ")), int(input("Enter number 3: "))
print(min (num1, num2, num3))




# Menu driven calculator

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
op = input("Enter the operator: ")

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
else:
    print(num1/num2)





# Guessing Game

import random as r
num = r.randint(1,100)
guess = int(input("Enter the number: "))
count = 1

while num != guess:
    if guess < num: 
        print("Wrong, guess higher")
    else:
        print("Wrong, guess lower")

    guess = int(input("Enter the number: "))
    count += 1

print("Correct Guess")
print("Turns = ",count)





# population of town is 10k, it is increasing at 10 percent per year. What is the population at the end of each year of the last 10 year.

pop = 10000

for i in range(0,10):
    pop = 1.1 * pop
    pop = pop//1
    print("Population at the end of", i+1, "year is", pop)