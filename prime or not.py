#prime number or not
def again():  
    number = int(input("Enter any number: "))

    if number > 1:
        for i in range(2, number):
            ((number/2) % i)
            
        if((number/2) % i == 0):    
            print(number, "is not a prime number")
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
    print("DO YOU WANT TO CONTINUE :")
    print("Choose Y/N for yes or no respectively:")
    choice = input()
    if(choice.upper() == "Y" ):
        replay()
    elif(choice.upper() == "N" ):
        exit()
    else:
        replay()


def replay():
        number = int(input("Enter any number: "))

        if number > 1:
            for i in range(2, number):
                ((number/2) % i)
            
            if((number/2) % i == 0):    
                print(number, "is not a prime number")
            else:
                print(number, "is a prime number")
        else:
            print(number, "is not a prime number")
            print("DO YOU WANT TO CONTINUE :")
            print("Choose Y/N for yes or no respectively:")
            choice = input()
            if(choice.upper() == "Y" ):
                again()
            elif(choice.upper() == "N" ):
                exit()

again()




