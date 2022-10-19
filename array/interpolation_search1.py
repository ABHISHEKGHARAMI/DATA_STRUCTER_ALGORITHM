#interpolation search
def interpolation_search(a,lo,hi,x):
    if lo<=hi:
        pos=lo+ (((x-a[lo])*(hi-lo))//(a[hi]-a[lo]))
        if a[pos]==x:
            return pos+1
        elif a[pos]>x:
            return interpolation_search(a,lo+1,pos-1,x)
        else:
            return interpolation_search(a,pos+1,hi,x)
a=list(map(int,input().split(' ')))
x=int(input())
t=interpolation_search(a,0,len(a)-1,x)
print(t)
