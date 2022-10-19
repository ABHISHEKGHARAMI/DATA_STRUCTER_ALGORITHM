#find the kth max and min in the array
n,k=map(int,input().split(" "))
arr=list(map(int,input().split(" ")))
arr1=sorted(arr)
print("\nThe {}th maximum number is :{}".format(k,arr1[len(arr1)-k]))
print("\nThe {}th minimum number is :{}".format(k,arr1[k-1]))
