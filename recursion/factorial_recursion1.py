#find the factorial of the number in the recursive way
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
print("The factorial of the given number is :",factorial(n))
