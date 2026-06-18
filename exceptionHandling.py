# Try Except Block

# reading a file which is not present --> Throws error

# with open('okaygoogle.txt','r') as f:
#     f.read()

# Traceback (most recent call last):
#   File "e:\pythonLearning\exceptionHandling.py", line 4, in <module>
#     with open('okaygoogle.txt','r') as f:
#          ~~~~^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'okaygoogle.txt'


try:
    with open('okaygoogle.txt','r') as f:
        f.read()
except:
    print("Sorry, file not found")