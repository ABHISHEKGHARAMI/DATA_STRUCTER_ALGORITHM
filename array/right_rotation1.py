#right rotate the array by one element
def right_rotate(a):
    n=len(a)
    temp=a[n-1]
    for i in range(n-1,-1,-1):
        a[i]=a[i-1]
    a[0]=temp
#right roate the array up to a certain number
def right_rotate_n(a,d):
    for i in range(d):
        right_rotate(a)
a=list(map(int,input().split(" ")))
right_rotate(a)
print(a)
b=list(map(int,input().split(" ")))
n=int(input("Enter the number to be rotate:"))
right_rotate_n(b,n)
print(b)
