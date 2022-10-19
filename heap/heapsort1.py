#heapsort in python using max heap
def heapify(a,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<len(a) and a[l]>a[largest]:
        largest=l
    if r<len(a) and a[r]>a[largest]:
        largest=r
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        heapify(a,n,largest)
#build the heapsort
def heapsort(a):
    n=len(a)
    for i in range(n//2-1,-1,-1):
        heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,n,0)
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print(arr[i])
