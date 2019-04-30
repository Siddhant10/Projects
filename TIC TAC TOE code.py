# Tic-Tac-Toe 

def header():
    print("""                                                                         
 To play Tic-Tac-Toe, you need to get three in a row...
 Your choices are defined, they must be from 1 to 9...

             SEQUENCE FOR THE TIC TAC TOE BOARD
                         1 | 2 | 3
                         4 | 5 | 6
                         7 | 8 | 9
 """)
import time
import random

table  = [" "," "," "," "," "," "," "," "," "," "]

def display_table():
    """GAME BOARD DISPLAY"""
    
    


    print("\n\t", table[1] , "|" , table[2] , "|" , table[3])
    print("\t","---------")
    print("\t",   table[4] , "|" , table[5], "|" ,table[6] )
    print("\t","---------")
    print("\t", table[7] , "|" , table[8] , "|" , table[9])

header()
while True:
    
    
    #player X
    options = input("please enter the choose for X from 1-9")
    options=int(options)
    

    #checking for empty space
    if table[options] == " ":
        
        table[options] = "X"
        display_table()
    else:
        print("not empty ")
        options = input("please enter the choose for X from 1-9")
        options=int(options)
        table[options] = "X"
        display_table()
        
        
    if(table[1] == "X" and table[2]=="X" and table[3]=="X") or\
            (table[4] == "X" and table[5]=="X" and table[6]=="X") or\
            (table[7] == "X" and table[8]=="X" and table[9]=="X") or\
            (table[1] == "X" and table[4]=="X" and table[7]=="X") or\
            (table[2] == "X" and table[5]=="X" and table[8]=="X") or\
            (table[3] == "X" and table[6]=="X" and table[9]=="X") or\
            (table[1] == "X" and table[5]=="X" and table[9]=="X") or\
            (table[3] == "X" and table[5]=="X" and table[7]=="X"):
            
            print ("X won")
    
        #tie
    isFull = True
    for index in range(1, 10):
        if table[index]==" ":
            isFull = False
            break

    if isFull == True:
       print(" TIE ")
       break
   
    #player O
    options = input("please enter the choose for O from 1-9")
    options=int(options)
    

    #checking for empty space
    if table[options] == " ":
        table[options] = "O"
        display_table()
        
    else:
        print("not empty")
        options = input("please enter the choose for O from 1-9")
        options=int(options)
        table[options] = "O"
        display_table()
        
    if(table[1] == "O" and table[2]=="O" and table[3]=="O") or\
            (table[4] == "O" and table[5]=="O" and table[6]=="O") or\
            (table[7] == "O" and table[8]=="O" and table[9]=="O") or\
            (table[1] == "O" and table[4]=="O" and table[7]=="O") or\
            (table[2] == "O" and table[5]=="O" and table[8]=="O") or\
            (table[3] == "O" and table[6]=="O" and table[9]=="O") or\
            (table[1] == "O" and table[5]=="O" and table[9]=="O") or\
            (table[3] == "O" and table[5]=="O" and table[7]=="O"):
            
            print (" O won")


print("WANT TO REPLAY : YES(Y)/NO(N):")
choice = input()



       
    

if(choice.upper() == "Y" ):
    import time
    import random

    table  = [" "," "," "," "," "," "," "," "," "," "]

    def display_table():
        """GAME BOARD DISPLAY"""
    
    


        print("\n\t", table[1] , "|" , table[2] , "|" , table[3])
        print("\t","---------")
        print("\t",   table[4] , "|" , table[5], "|" ,table[6] )
        print("\t","---------")
        print("\t", table[7] , "|" , table[8] , "|" , table[9])

    while True:
    
    
        #player X
        options = input("please enter the choose for X from 1-9")
        options=int(options)
    

        #checking for empty space
        if table[options] == " ":
        
            table[options] = "X"
            display_table()
        else:
            print("not empty ")
            options = input("please enter the choose for X from 1-9")
            options=int(options)
            table[options] = "X"
            display_table()
        
        
        if(table[1] == "X" and table[2]=="X" and table[3]=="X") or\
                (table[4] == "X" and table[5]=="X" and table[6]=="X") or\
                (table[7] == "X" and table[8]=="X" and table[9]=="X") or\
                (table[1] == "X" and table[4]=="X" and table[7]=="X") or\
                (table[2] == "X" and table[5]=="X" and table[8]=="X") or\
                (table[3] == "X" and table[6]=="X" and table[9]=="X") or\
                (table[1] == "X" and table[5]=="X" and table[9]=="X") or\
                (table[3] == "X" and table[5]=="X" and table[7]=="X"):
            
                print ("X won")
    
            #tie
        isFull = True
        for index in range(1, 10):
            if table[index]==" ":
                isFull = False
                break

        if isFull == True:
            print(" ")
            break
   
        #player O
        options = input("please enter the choose for O from 1-9")
        options=int(options)
    

        #checking for empty space
        if table[options] == " ":
            table[options] = "O"
            display_table()
        
        else:
            print("not empty")
            options = input("please enter the choose for O from 1-9")
            options=int(options)
            table[options] = "O"
            display_table()
        
        if(table[1] == "O" and table[2]=="O" and table[3]=="O") or\
                (table[4] == "O" and table[5]=="O" and table[6]=="O") or\
                (table[7] == "O" and table[8]=="O" and table[9]=="O") or\
                (table[1] == "O" and table[4]=="O" and table[7]=="O") or\
                (table[2] == "O" and table[5]=="O" and table[8]=="O") or\
                (table[3] == "O" and table[6]=="O" and table[9]=="O") or\
                (table[1] == "O" and table[5]=="O" and table[9]=="O") or\
                (table[3] == "O" and table[5]=="O" and table[7]=="O"):
            
                print (" O won")

elif (choice.upper() == "N"):
    exit()
else:
    print("CHOOSE BETWEEN Y AND N")
    print("WANT TO REPLAY : YES(Y)/NO(N):")
    choice = input()



       
    

    if(choice.upper() == "Y" ):
        import time
        import random

        table  = [" "," "," "," "," "," "," "," "," "," "]

        def display_table():
            """GAME BOARD DISPLAY"""
    
    


            print("\n\t", table[1] , "|" , table[2] , "|" , table[3])
            print("\t","---------")
            print("\t",   table[4] , "|" , table[5], "|" ,table[6] )
            print("\t","---------")
            print("\t", table[7] , "|" , table[8] , "|" , table[9])

        while True:
    
    
            #player X
            options = input("please enter the choose for X from 1-9")
            options=int(options)
    

            #checking for empty space
            if table[options] == " ":
            
                table[options] = "X"
                display_table()
            else:
                print("not empty ")
                options = input("please enter the choose for X from 1-9")
                options=int(options)
                table[options] = "X"
                display_table()
        
        
            if(table[1] == "X" and table[2]=="X" and table[3]=="X") or\
                    (table[4] == "X" and table[5]=="X" and table[6]=="X") or\
                    (table[7] == "X" and table[8]=="X" and table[9]=="X") or\
                    (table[1] == "X" and table[4]=="X" and table[7]=="X") or\
                    (table[2] == "X" and table[5]=="X" and table[8]=="X") or\
                    (table[3] == "X" and table[6]=="X" and table[9]=="X") or\
                    (table[1] == "X" and table[5]=="X" and table[9]=="X") or\
                    (table[3] == "X" and table[5]=="X" and table[7]=="X"):
            
                    print ("X won")
    
                #tie
            isFull = True
            for index in range(1, 10):
                if table[index]==" ":
                    isFull = False
                    break

            if isFull == True:
                print(" ")
                break
   
            #player O
            options = input("please enter the choose for O from 1-9")
            options=int(options)
        

            #checking for empty space
            if table[options] == " ":
                table[options] = "O"
                display_table()
            
            else:
                print("not empty")
                options = input("please enter the choose for O from 1-9")
                options=int(options)
                table[options] = "O"
                display_table()
        
            if(table[1] == "O" and table[2]=="O" and table[3]=="O") or\
                    (table[4] == "O" and table[5]=="O" and table[6]=="O") or\
                    (table[7] == "O" and table[8]=="O" and table[9]=="O") or\
                    (table[1] == "O" and table[4]=="O" and table[7]=="O") or\
                    (table[2] == "O" and table[5]=="O" and table[8]=="O") or\
                    (table[3] == "O" and table[6]=="O" and table[9]=="O") or\
                    (table[1] == "O" and table[5]=="O" and table[9]=="O") or\
                    (table[3] == "O" and table[5]=="O" and table[7]=="O"):
            
                    print (" O won")

            elif (choice.upper() == "N"):
                exit()



    
            


