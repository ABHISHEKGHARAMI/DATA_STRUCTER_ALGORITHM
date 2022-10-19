#1. 1's compliment
#2. 2's compliment
def ones_comp(a):
    if a>0:
        return ~a
#
def two_comp(a):
    if a>0:
        return ~a+1
a=int(input())
print("Ones compliment is : ",ones_comp(a))
print("Twos compliment is : ",two_comp(a))
