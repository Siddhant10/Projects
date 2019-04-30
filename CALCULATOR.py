import statistics
def again():
    try:
        global number1
        number1 = int(input("Give the first number: "))
    except ValueError:
        print('That is not an number!!')

try:
    number1 = int(input("Give the first number: "))
except ValueError:
    print('That is not an number!!')
    again()

try:
    number2 = int(input("Give the second number: "))
except ValueError:
    print('That is not an number!!')
    again()
    
    try:
        number2 = int(input("Give the second number: "))
    except ValueError:
        print('That is not an number!!')
        again()


def add():
    print("ADDITION", number1 + number2)

def sub():
    print("SUBTRACTION", number1 - number2)

def mul():
    print("MULTIPLICATION", number1 * number2)

def div():
    print("DIVISION", number1 / number2)



while True:   
     print("(1) Choose 1 for additon \n(2) Choose 2 for subtraction\n(3) Choose 3 for multipication\n(4) Choose 4 for division\n(5)Choose 5 for quit")
     print("Selected numbers:",number1,number2)
     operation = input("Choose (1-5): ")
    
 



     if operation == '1':
        
        add()
    

     elif operation == '2':
        
        sub()
        
     elif operation == '3':
        
        mul()
        
     elif operation == '4':
        
        div()
       
        
     elif operation == '5':

        quit()
     else:
         print("INVALID OPERATION")


