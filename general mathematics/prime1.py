#check the number is prime or not
import math 
def prime(a):
    flag=0
    n=math.sqrt(a)
    for i in range(2,int(n)):
        if a%i==0:
            flag=1
            break
    if flag==0:
        print("A prime number.")
    else:
        print("Not a prime number.")
a=int(input())
prime(a)
            
