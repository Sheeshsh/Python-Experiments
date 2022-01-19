print("***********YASH NITIN KAMBLE************")
def change_char (str1):
      if str1[0].isupper()==True:
          lower = str1.lower()
          char = lower[0]
          str1 = lower.replace (char, '$')
          str1 = char + str1[1:]
          capital = str1.capitalize()
          return capital
      else:
          char = str1[0]
          str1 = str1.replace (char, '$')
          str1 = char + str1[1:]
          return str1 
word = input("Enter a string:")
print (change_char(word))
