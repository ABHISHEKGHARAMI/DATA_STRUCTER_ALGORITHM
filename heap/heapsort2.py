#building the heapsort using min heap
#runtime of the heapsort will be O(nlogn)
def heapify(a,n,k):
    smallest=k
    l=2*k+1
    r=2*k+2
    if l<len(a) and a[l]<a[smallest]:
        smallest=l
    if r<len(a) and a[r]<a[smallest]:
        smallest=r
    if smallest!=k:
        a[smallest],a[k]=a[k],a[smallest]
        heapify(a,n,smallest)
#get the heapsort

def heapsort(a):
    n=len(a)
    for i in range(n//2-1,-1,-1):
        heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heapify(a,n,0)
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print(arr[i])
        
    
