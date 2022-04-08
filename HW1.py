def main():
    q = int(input("Enter question number\n\r"))
    if q == 1:
        # Question 1 - Your code should print the Collatz sequence (as a list of integers) starting at a and ending at 1.
        # WRITE YOUR CODE HERE.
        Flag = 1
        while Flag:                     #All the extreame cases problem.
            a = (input("Enter a\n\r"))
            if a.isnumeric():
                a = int(a)
                Flag = 0
            else:
                print("Please enter an int , a>0")
                continue
            if int(a) == 0:
                print ("0 will not work in this case.")
                Flag = 1
                                         # The Collatz conjecture starts here!
        Element_List = []                # Empty list
        Element_List.append(a)
        while (a != 1):
            if (a%2 == 0):               #For even
                a /= 2
                Element_List.append(int(a))
            else:
                a = a*3 + 1              #For odd
                Element_List.append(int(a))
        print (Element_List)             #The whole list

    elif q == 2:
    # Question 2 - Your code should print the Caesar encryption of the string x defined by the number of shifts specified in the parameter shift
        x = str(input("Enter text\n\r"))
        shift = int(input("Enter shift integer\n\r"))
        # WRITE YOUR CODE HERE.
        x = list(x)                                #Convert word to char list
        x = [ord(i) for i in x]                    #Convert every char to ascii value
        x = [i + shift for i in x]                 #Add the value of shift for every ascii value
        Fact = 0                                   #Factorial variable for while loop
        while Fact < len(x):
            while x[Fact] > 126 or x[Fact] < 32:   #Check every value in 32<i<126
                if x[Fact] > 126:
                    x[Fact] = (x[Fact] - 95 )
                else:
                    x[Fact] = x[Fact] + 95
            Fact += 1
        x = [chr(i) for i in x]                    #Convert to char
        print(''.join(x))                          #Merge char to string





    elif q == 3:
        # Question 3 - Your code should print the longest palindromic substring in x.
        x = str(input("Enter a string\n\r"))
        x = list(x)                              #Convert word to char list
        Stack = []                               #This is the cartridge of the palindrom list
        for i in range(len(x)):                  #External loop
            for j in range(i+1, len(x)+1):       #Internal loop
                Check = x[i:j]                   #Slice every element from external loop to internal loop and save the slice in "Check"
                if Check == Check[::-1]:         #Compare the slice with the reverse (palindrom).
                    Stack.append(Check)          #If the slice is similar to reverse save the word in Stack
        Longest_Palindrom = max(Stack , key=len) #Take the longest Palindrom from Stack
        print(''.join(Longest_Palindrom))        #Merge the list to one word


    else:
        pass


if __name__ == '__main__':
    main()