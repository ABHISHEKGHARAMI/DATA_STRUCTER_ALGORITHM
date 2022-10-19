#Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
n=int(input())
arr=list(map(int,input().split(" ")))
low=0
mid=0
hi=len(arr)-1
while mid<=hi:
    if arr[mid]==0:
        arr[low],arr[mid]=arr[mid],arr[low]
        low=low+1
        mid=mid+1
    elif arr[mid]==1:
        mid=mid+1
    else:
        arr[mid],arr[hi]=arr[hi],arr[mid]
        hi=hi-1
print("\nThe sorted array is :",arr)
