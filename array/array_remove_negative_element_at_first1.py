def remove_element(a):
    n=len(a)
    pos=[]
    neg=[]
    for i in range(n):
        if a[i]<0:
            pos.append(a[i])
        else:
            neg.append(a[i])
    sorted(neg)
    for i in range(len(pos)):
        neg.append(pos[i])
    print(neg)
a=list(map(int,input().split(" ")))
remove_element(a)
print(a)
