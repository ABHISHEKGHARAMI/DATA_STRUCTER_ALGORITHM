#this program will put all the zero at the end of the program
def move_zero(a):
    n=len(a)
    count=0
    for i in range(n):
        if a[i]!=0:
            a[count]=a[i]
            count+=1
    while count<n:
        a[count]=0
        count+=1
arr=list(map(int,input().split(" ")))
move_zero(arr)
print(arr)
