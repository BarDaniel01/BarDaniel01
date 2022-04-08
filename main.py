def main():
    q = int(input("Enter question number\n\r"))
    if q == 1:
        # Question 1 - Your code should print the Collatz sequence (as a list of integers) starting at a and ending at 1.
        Flag = 1
        while Flag:    #All the extreame cases problem.
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
        Element_List = []
        Element_List.append(a)
        while (a != 1):
            if (a%2 == 0):
                a /= 2
                Element_List.append(int(a))
            else:
                a = a*3 + 1
                Element_List.append(int(a))
        print (Element_List)

    elif q == 2:
    # Question 2 - Your code should print the Caesar encryption of the string x defined by the number of shifts specified in the parameter shift
        x = str(input("Enter text\n\r"))
        shift = int(input("Enter shift integer\n\r"))
        # WRITE YOUR CODE HERE.

    elif q == 3:
        # Question 3 - Your code should print the longest palindromic substring in x.
        x = str(input("Enter a string\n\r"))
        # WRITE YOUR CODE HERE.

    else:
        pass


if __name__ == '__main__':
    main()