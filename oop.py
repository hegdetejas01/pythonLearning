# PascalCase - start the first letter of all the word in Capital
class Atm:

    def __init__ (self):
        print(id(self))
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi, How can I help you?
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. press anything else to exit     
        """)

        if user_input == '1':
            self.createPin()
        elif user_input == '2':
            self.changePin()
        elif user_input == '3':
            self.checkBalance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def createPin(self):
        userPin = input("enter new pin: ")
        self.pin = userPin
        userBalance = int(input("enter your balance: "))
        self.balance = userBalance
        print("Pin created successfully")
        self.menu()

    def changePin(self):
        oldPin = input("enter your old pin: ")
        if oldPin == self.pin:
            newPin = input("Enter new pin: ")
            self.pin = newPin
            print("Pin changed succesfully")
        else:
            print("Old pin is wrong")
        self.menu()

    def checkBalance(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            print("Your balance is", self.balance)
        else: print("Wrong Pin")
        self.menu()

    def withdraw(self):
        yourPin = input("Enter your pin: ")
        if yourPin == self.pin:
            withdrawAmount = int(input("How much you want to withdraw: "))
            if withdrawAmount > self.balance:
                print("Insufficient Balance")
            else:
                self.balance -= withdrawAmount
                print("Withdrawl Success")
            
            print("Your Current Balance is", self.balance)

        else:
            print("Wrong Pin")

        self.menu()

# obj = Atm()
# print(id(obj))





# Creating a new data type - fraction
class Fraction:
    """
    numerator, denominator
    """
    def __init__(self, x, y): # parameterised constructor i.e the constructor which needs input
        self.numerator = x
        self.denominator = y

    def __str__(self):
        # return "i am here"
        return "{}/{}".format(self.numerator, self.denominator)
    
    def __add__(self,other): # self = fr1, other = fr2
        # print("i am here")
        newNumerator = (self.numerator*other.denominator) + (other.numerator*self.denominator)
        newDenominator = self.denominator * other.denominator
        return "{}/{}".format(newNumerator, newDenominator)
    
    def __sub__(self,other): 
        newNumerator = (self.numerator*other.denominator) - (other.numerator*self.denominator)
        newDenominator = self.denominator * other.denominator
        return "{}/{}".format(newNumerator, newDenominator)
    
    def __mul__(self,other): 
        newNumerator = self.numerator * other.numerator
        newDenominator = self.denominator * other.denominator
        return "{}/{}".format(newNumerator, newDenominator)
    
    def __truediv__(self,other): 
        newNumerator = self.numerator * other.denominator
        newDenominator = self.denominator * other.numerator
        return "{}/{}".format(newNumerator, newDenominator)
    
    def convertToDecimal(self):
        return self.numerator/self.denominator

fr1 = Fraction(3,4)
fr2 = Fraction(1,2)
print(fr1, fr2)

a = fr1 + fr2
b = fr1 - fr2
c = fr1 * fr2
d = fr1 / fr2
print(a,b,c,d,sep="\n")

e = fr1.convertToDecimal()
print(e)












