#building the min heap from the scratch
def min_heapify(a,k):
    l=left(k)
    r=right(k)
    if l<len(a) and a[l]<a[k]:
        smallest=l
    else:
        smallest=k
    if r<len(a)  and a[r]<a[smallest]:
        smallest=r
    if smallest!=k:
        a[smallest],a[k]=a[k],a[smallest]
        min_heapify(a,smallest)
#get the left
def left(k):
    return 2*k+1
#get right
def right(k):
    return 2*k+2
#build the min heap
def build_min_heap(a):
    n=int(len(a)//2)-1
    for k in range(n,-1,-1):
        min_heapify(a,k)

n=int(input("Enter the number of the element:"))
print("\nEnter element:")
a=list(map(int,input().split(" ")))
build_min_heap(a)
print(a)
