#jump search in the array
import math
def jump_search(a,x):
    n=len(a)
    step=math.sqrt(n)
    prev=0
    while a[int(min(step,n))-1]<x:
        prev=step
        step+=math.sqrt(n)
        if prev>=n:
            return -1
    while a[int(prev)]<x:
        prev+=1
        if prev==min(step,n):
            return -1
    if a[int(prev)]==x:
        return prev
    return -1
a=list(map(int,input().split(' ')))
x=int(input())
t=jump_search(a,x)
print(t+1)
