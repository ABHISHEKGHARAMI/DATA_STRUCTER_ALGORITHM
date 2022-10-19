#n's compliment of a gien number
def count_digit(a):
    if a==0:
        return 0
    else:
        return 1+count_digit(a//10)
#n's compliment
def n_s_compliment(a,n):
    n1=count_digit(a)
    sum=0
    for i in range(n1):
        sum=sum*10+n
    print(sum)
    print(n1)
    s1=sum-a
    s1+=1
    return s1
a=int(input())
n=int(input())
print("n' s compliment of a gien number: ",n_s_compliment(a,n))
