#taylor series
#e^x=1+x/1 + x^2/2!+...............+x^n/n!
#1. recurrsence of the sum
def recur_sum(n):
    if n==0:
        return 0
    else:
        return n+recur_sum(n-1)
#2. recursenece of the factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
#3. power recurense of the number
def power(n,k):
    if k==0:
        return 1
    else:
        return n*power(n,k-1)
#4. Taylor function for the main function
def taylor_sum(n):
    if n==0:
        return 1
    else:
        return (power(n,n)/factorial(n))+taylor_sum(n-1)
n=int(input())
print("\nThe evaluation of the taylor function :",taylor_sum(n))

