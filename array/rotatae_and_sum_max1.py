#find the max sum of i*arr[i] from the array rotation
def rotate_by_one(a):
    n=len(a)
    temp=a[0]
    for i in range(n-1):
        a[i]=a[i+1]
    a[n-1]=temp
#get the max sum
def sum_rotate(a):
    n=len(a)
    sum=0
    res=0
    for i in range(n-1):
        rotate_by_one(a)
        for j in range(len(a)-1):
            res=res+j*a[j]
        if sum<res:
            sum=res
    return sum
a=list(map(int,input().split(" ")))
b=sum_rotate(a)
print(b)
