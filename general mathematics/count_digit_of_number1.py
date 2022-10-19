#count the total number of a given number
def count_number(a):
    if a==0:
        return 0
    else:
        return 1+count_number(a//10)
def alter(a):
    sum=0
    while a:
        sum+=1
        a=a//10
    return sum
a=int(input())
print(count_number(a))
print(alter(a))
