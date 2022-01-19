print("***********YASH NITIN KAMBLE************")
while(1):
    print("1.Number Palindrome\n2.String Palindrome\n3.EXIT\n")
    choice=input("ENTER YOUR CHOICE:")
    ch=int(choice)
    if(ch==1):
        number=int(input("Enter any number :"))
        temp=number #storing number in temp variable
        reverse_num=0
        while(number>0):
            digit=number%10 
            reverse_num=reverse_num*10+digit
            number=number//10
        if(temp==reverse_num):
            print("The number is palindrome!")
        else:
            print("Not a palindrome!")
    elif(ch==2):
        string = input('Enter the string: ')
        i=0
        for i in range(len(string)):
           if string[i]!=string[-1-i]:
              print(string,'is not a Palindrome')
              break
           else:
              print(string,'is a Palindrome')
              break
    else:
        exit()
