import sys

allowedOperators = ['+', '-', '*', '/']
allOk = False

while not allOk :

    num1 = input("Enter a number (or a letter to exit): ")
    if len(num1) == 1 and num1.isalpha() :
        print("Exiting.")
        sys.exit()

    try :
        val1 = int(num1)
    except ValueError :
        print("Invalid sign.")
    else :
        allOk = True

allOk = False
while not allOk :
    operation = input("Enter an operation: ")
    if operation in allowedOperators :
        allOk = True
    else :
        print("Invalid sign.")

allOk = False
while  not allOk :

    num2 = input("Enter another number: ")
    try :
        val2 = int(num2)
    except ValueError :
        print("Invalid sign.")
    else :
        allOk = True

if operation == '+' :
    result = val1 + val2
elif operation == '-' :
    result = val1 - val2
elif operation == '*' :
    result = val1 * val2
elif operation == '/' :
    result = val1 / val2

print("Result: {}".format(result))
