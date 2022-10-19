#reverse the array with
n=int(input("Enter the number of element to be insert:"))
arr=list(map(int,input().split(" ")))
start=0
end=len(arr)-1
while(start<end):
    arr[start],arr[end]=arr[end],arr[start]
    start=start+1
    end=end-1
print("the reversed array is:",arr)
