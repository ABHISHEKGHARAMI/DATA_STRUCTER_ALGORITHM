#binary search
def binary_search(a,s,e,x):
    if s<=e:
        mid=(s+e)//2
        if a[mid]==x:
            return mid+1
        elif a[mid]>x:
            return binary_search(a,s+1,mid-1,x)
        else:
            return binary_search(a,mid+1,e-1,x)
a=list(map(int,input().split(' ')))
s=0
e=len(a)-1
x=int(input())
t=binary_search(a,s,e,x)
print(t)
