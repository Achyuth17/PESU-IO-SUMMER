num=input("Enter the numbers:").split(",")
n=[]
for i in num:
    i=int(i)
    n.append(i)
print(n)
t=tuple(n)
print(t)
