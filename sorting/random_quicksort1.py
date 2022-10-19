#randomize version of quicksort
#using lamuto partitioning
import random
def quicksort(a,low,high):
    if low<high:
        p=partition_random(a,low,high)
        quicksort(a,low,p-1)
        quicksort(a,p+1,high)
#partion random
def partition_random(a,low,high):
    r=random.randrange(low,high)
    a[r],a[low]=a[low],a[r]
    return partition(a,low,high)
#partition the main
def partition(arr,start,stop):
    pivot = start # pivot
     
    # a variable to memorize where the
    i = start + 1
     
    # partition in the array starts from.
    for j in range(start + 1, stop + 1):
         
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
n=int(input("Enter the number of element:"))
print("Enter element:")
a=list(map(int,input().split(" ")))
quicksort(a,0,len(a)-1)
print(a)
