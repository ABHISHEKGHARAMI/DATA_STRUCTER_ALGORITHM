#odd the smaller and even the bigger
def array_replace(a):
    n=len(a)
    for i in range(n-1):
        if i==0 and a[i]>=a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
        if i!=0 and a[i]<=a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
a=list(map(int,input().split(',')))
array_replace(a)
print(a)
