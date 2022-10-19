#counting sort using the python
def countingSort(a):
    size=len(a)
    output=[0]*size
    #intialize the count array
    count=[0]*10

    #count each of the element
    for i in range(0,size):
        count[a[i]]+=1
    #store the cummulative sum of the array
    for i in range(1,10):
        count[i]+=count[i-1]
    #find the index of the element
    i=size-1
    while i>=0:
        output[count[a[i]-1]]=a[i]
        count[a[i]]-=1
        i-=1
    #copy each element in the arrayback
    for i in range(0,size):
        a[i]=output[i]
#calling the main function
data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
