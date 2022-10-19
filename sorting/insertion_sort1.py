#optimize insertion sort in python

def insertionSort(a,size):
    for i in range(1,size):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
#calling the main function

data = [-2, 45, 0, 11, -9]
size = len(data)
insertionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
