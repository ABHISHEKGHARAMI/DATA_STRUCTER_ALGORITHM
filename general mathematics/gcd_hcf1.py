#find the gcd or the hcf of the given number
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,b%a)
a,b=map(int,input().split(','))
print('Gcd is :',gcd(a,b))
def hcf(a,b):
    t=gcd(a,b)
    return (a*b)//t
print("Hcf is :",hcf(a,b))
