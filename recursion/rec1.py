#function program to find the recursion and print the recursion
def func(n):
    if n>0:
        print(n,end=" ")
        func(n-1)
def func1(n):
    if n>0:
        func1(n-1)
        print(n,end=" ")
#sum function
def sum_recursive(n):
    if n==0:
        return 0
    else:
        return n+sum_recursive(n-1)
        
n=int(input("Enter the digit:"))
func(n)
print("\nAfter calling the second function:\n")
func1(n)
print("\nThe sum of the recursion will be:",sum_recursive(n))
