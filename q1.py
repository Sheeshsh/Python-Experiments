print("***********YASH NITIN KAMBLE************")
import numpy as np
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
    ele = str(input())
    lst.append(ele) # adding the element
print("List of Colors:",lst)
print("First Color:",lst[0],"\nand Last Color:",lst[-1])
print("Unique List of color:",np.unique(lst))



'''
colors = input("Enter list of colors:")
lst = colors.split()      #split() converts String to List.
print(lst,type(lst))
print("First color:",lst[0])
print("Last Color is:",lst[-1])
print(np.unique(lst))'''

'''
print("********* PartI **********")
colors = ['Red','Cyan','White','Maroon','Crimson','Purple']
print(colors,type(colors))
print("First color:",colors[0])
print("Last Color is:",colors[-1]) '''



