#program to show the indirect recurssion
def func1(n):
    if n>0:
        print(n,end=" ")
        func2(n-1)
#calling the second func to first function
def func2(n):
    if n>1:
        print(n,end=" ")
        func1(n//2)
n=int(input())
func1(n)
