#find the max and the min in the array
n=int(input())
arr=list(map(int,input().split(" ")))
arr1=sorted(arr)
print("\nThe maximum number in the array is ",arr1[len(arr1)-1])
print("\nThe minimum number in the array is ",arr1[0])
