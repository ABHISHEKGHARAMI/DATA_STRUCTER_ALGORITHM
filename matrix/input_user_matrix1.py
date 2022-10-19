m=int(input("Enter number of rows:"))
n=int(input("Enter number of column"))
mat=[]
for i in range(m):
    a=[]
    for j in range(n):
        a1=int(input())
        a.append(a1)
    mat.append(a)
def print1(mat,m,n):
    for i in range(m):
        for j in range(n):
            print("\t",mat[i][j])
        print("\n")
def upper_traingle_copy(mat,m,n):
    for i in range(m):
        for j in range(n):
            if i!=j:
                mat[i]
upper_traingle_copy(mat,m,n)
        
