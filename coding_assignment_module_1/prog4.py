no=int(input("Enter a no:"))
sum=0
while(no>0):
    digit=no%10
    sum+=digit
    no=no//10
print(sum)

