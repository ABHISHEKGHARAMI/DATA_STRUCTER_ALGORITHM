#building the max and min heap from the scratch
def max_heapify(a,k):
    l=left(k)
    r=right(k)
    if l<len(a) and a[l]>a[k]:
        largest=l

    else:
        largest=k
    if r<len(a) and a[r]>a[largest]:
        largest=r
    if largest!=k:
        a[k],a[largest]=a[largest],a[k]
        max_heapify(a,largest)
#get the left
def left(k):
    return 2*k+1
#get the right
def right(k):
    return 2*k+2
#build the max heap
def build_max_heap(a):
    n=int(len(a)//2)-1
    for k in range(n,-1,-1):
        max_heapify(a,k)
#heapsort
def heapsort(a):
    n=len(a)
    build_max_heap(a)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        max_heapify(a,0)
n=int(input("Enter the number of the element:"))
print("\nEnter element:")
a=list(map(int,input().split(" ")))
build_max_heap(a)
print(a)
heapsort(a)
print(a)
