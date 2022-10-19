#rotate an element by one
def rotate_by_one(a):
    n=len(a)
    temp=a[0]
    for i in range(n-1):
        a[i]=a[i+1]
    a[n-1]=temp
#left rotate by several element
def rotate_by_several(a,d):
    for i in range(d-1):
        rotate_by_one(a)
a=list(map(int,input().split(" ")))
rotate_by_one(a)
print(a)
n=int(input("Enter the number to be rotate:"))
rotate_by_several(a,n)
print(a)
