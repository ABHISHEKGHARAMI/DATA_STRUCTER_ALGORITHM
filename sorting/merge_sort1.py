#mergesort in pyton using devide and conquere algorithm with runtime 0(nlogn) time space complexity 0(1)
def mergesort(a):
    if len(a)>1:
        q=len(a)//2
        l=a[:q]
        r=a[q:]
        mergesort(l)
        mergesort(r)
        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i]<r[j]:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while i < len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j < len(r):
            a[k]=r[j]
            j+=1
            k+=1
#calling the main function

data = [-2, 45, 0, 11, -9]
size = len(data)
mergesort(data)
print('Sorted Array in Ascending Order:')
print(data)
