#!/usr/bin/env python3
# A program that prompts a user for two operators and and operation (plus or minus)
# the program then shows the result.
# The user may enter 'q' to exit the program.
while (True):
    a = input('What is the first operator? or, enter q to quit: ')
    if a.lstrip("-").lstrip(".").isnumeric(): 
        op1 = float(a)
    else:
        op1 = a.lower()
        if ( op1 == 'q' ):
            print("You have asked to quit.  Goodbye!")
            break
        else:
            print("You name entered a non-numeric value...exiting")
            break
        
    b = input('What is the second operator? or, enter q to quit: ')
    if b.isnumeric():
        op2 = float(b)
    else:
        op2 = b.lower()
        if ( op2 == 'q' ):
            print("You have asked to quit.  Goodbye!")
            break
        else:
            print("You name entered a non-numeric value...exiting")
            break

    o = input('Enter the operation to perform on the two operators (+ or -): ')
    if o == '+':
        print(int(op1) + int(op2))
     
    elif o == '-':
        print(int(op1) - int(op2))
    else:
        print("This is an invalid operation...restarting")
