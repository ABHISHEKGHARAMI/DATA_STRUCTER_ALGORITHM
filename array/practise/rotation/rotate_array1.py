#rotate the array
def rotate(l,n,d):
    k=l.index(d)
    l1=[]
    l1=l[k+1:n]+l[0:k+1]
    return l1

n=int(input("enter the number of array:"))
l=[]
for i in range(n):
    a=int(input("enter the data:"))
    l.append(a)
d=int(input("enter the number of times of rotate:"))
print(rotate(l,n,d))

