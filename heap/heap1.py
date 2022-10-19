#this program will return the max and min of the heap
import heapq
n=int(input("Enter the number of element:"))
li=list(map(int,input().split(" ")))
heapq.heapify(li)
print(li)
