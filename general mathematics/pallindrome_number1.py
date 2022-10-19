#check number is palindrome or not
def pallindrome(a):
    temp=a
    sum=0
    while a>0:
        rem=a%10
        sum=sum*10+rem
        a=a//10
    if sum==temp:
        print("Yes it is a pallindrome number.")
    else:
        print("This does not in the pallindrome number.")
a=int(input())
pallindrome(a)
