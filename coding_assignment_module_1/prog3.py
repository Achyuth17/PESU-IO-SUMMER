li=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
    a=int(input("Enter in ascending order:"))
    li.append(a)
print(li)
ele=int(input("Enter the no to be checked:"))
low=0
high=n
def binary(low,high,ele):
    mid=(low+high)//2
    if low<=high:

        if li[mid]==ele:
            print("The no ",ele,"is found at position",li.index(ele))
        elif li[mid]>ele:
            high=mid-1
            return binary(low,high,ele)
        else:
            low=mid+1
            return binary(low,high,ele)
    else:
        print("The no ",ele,"is not found ")
binary(low,high,ele)
