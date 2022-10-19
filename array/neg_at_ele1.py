#put all negative element at the last of the array
def put_list(a):
    count=0
    pos=[]
    neg=[]
    for i in range(len(a)):
        if a[i]>0:
            pos.append(a[i])
        else:
            neg.append(a[i])
    for i in range(len(pos)):
        a[i]=pos[i]
        count+=1
    j=0
    while count<len(a):
        a[count]=neg[j]
        j+=1
        count+=1
arr=list(map(int,input().split(" ")))
put_list(arr)
print(arr)
