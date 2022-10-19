#bubble sort for a given array in python
import time 
def bubble_sort(a):
    n=len(a)
    start=time.time()
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    end=time.time()
    print(end-start)

#calling the main function
n=int(input("Enter the number of element:"))
print("Enter element:")
a=list(map(int,input().split(" ")))
bubble_sort(a)
print("After the bubble sort the array will be:")
for i in range(len(a)):
    print(a[i],end=" ")
#
