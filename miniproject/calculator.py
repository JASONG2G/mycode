#!/usr/bin/env python3

'''
Author: Jason 

This program is a calculator which perform adds/subtracts/divides/multiplies.

'''

flag = False # initialize flag to False as a switch to break out of while loop.

# helper functions 
# addition  
def add(a, b):
    print(a + b)

# subtraction 
def sub(a, b):
    print( a - b)

# divide
def div(a, b):
    print(a / b)

# multipile
def multi(a, b):
    print(a * b)

# the main function

def main():
    '''the main program'''
    while(True and flag == False):
        try:
            print('Please enter the first operand.')
            ops1 = float(input(">").strip())
            print('Please enter the second operand.')
            ops2 = float(input(">").strip())
            print('''
                    Choose an operation you want:
                    1: add
                    2: subtract
                    3: divide
                    4: multipile
                    5: exit
                    ''')
            ops3 = int(input('>').strip())
        except:
            print("0_o something is wrong, please try again.")
        
        # call operation base on user input
        if ops3 == 1:
            add(ops1, ops2)
        elif ops3 == 2:
            sub(ops1,ops2)
        elif ops3 == 3:
            div(ops1,ops2)
        elif ops3 == 4:
            multi(ops1,ops2)
        elif ops3 == 5:
            exit()
        else:
            print('the option does not exist, please try again.')
        
        more()


def more():
    while True:
        print("would you like to do another operation? Y/N")
        try:
            option = input(">").strip().lower()
        except:
            print("0_o not an option, please try again.")
            more()
        if option == 'y':
            main()
        else: 
            exit()

# call the main function

if __name__ == "__main__":
    main()

