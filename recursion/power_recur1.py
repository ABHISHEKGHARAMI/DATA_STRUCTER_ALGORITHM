#find the power using recursion
def power_recur(n,k):
    if k==0:
        return 1
    else:
        return n*power_recur(n,k-1)
print("\nEnter the base and power :")
n,k=map(int,input().split(" "))
print("\nThe result is: ",power_recur(n,k))
