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
