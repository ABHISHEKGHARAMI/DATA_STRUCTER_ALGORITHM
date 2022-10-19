#replace all the negative  element in the corner
n=int(input())
arr=list(map(int,input().split(" ")))

j=0
for i in range(0,n):
    if arr[i]<0:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        j=j+1
print("\nThe sorted out array is :",arr)
