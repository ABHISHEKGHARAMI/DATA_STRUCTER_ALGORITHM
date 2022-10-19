#linear search
def linear_search(a,x):
    n=len(a)
    for i in range(n):
        if a[i]==x:
            return i+1
            break
a=list(map(int,input().split(" ")))
x=int(input())
t=linear_search(a,x)
print(t)
    
