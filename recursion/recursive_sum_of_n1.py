#find the sum of the n number using recursion
def sum_recur1(n):
    sum=0
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+sum_recur1(n-1)
n=int(input())
print("The sum of the recursion is: ",sum_recur1(n))
