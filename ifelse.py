reqEmail = "tejashegde@"
reqPass = "1234"

userEmail, userPass = input("Enter Email: "), input("Enter Password: ")
if userEmail == reqEmail and userPass == reqPass:
    print("Login Successfull")
elif userEmail == reqEmail and userPass != reqPass:
    print("Incorrect Password")
    userPass = input("Enter the password: ")
    if userPass == reqPass: 
        print("Login Successfull")
    else: 
        print("Wrong Passwords")
else:
    print("Incorrect Password or Email")

print("Everything Done")
