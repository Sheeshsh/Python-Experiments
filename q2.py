print("***********YASH NITIN KAMBLE************")
x=int(input("Enter range of tuple:"))
i=0
t=()
p=[]
while(i<x):
    i+=1
    y=int(input("Enter the number:"))
    p.append(y)
    t=tuple(p)
    
for i in range(0,len(t)):
    print ( "{} is repeated {}".format(t[i],t.count(t[i])))




