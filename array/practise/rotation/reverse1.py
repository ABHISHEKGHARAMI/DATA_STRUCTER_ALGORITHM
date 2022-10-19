#reverse array
def reverse(a,s,l):
    while s<l:
        temp=a[s]
        a[s]=a[l]
        a[l]=temp
        s=+1
        l=-1
    return a
print(reverse([1,2,3,4],0,4))
    
