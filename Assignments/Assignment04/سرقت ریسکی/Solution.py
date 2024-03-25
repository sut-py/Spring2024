import random
#max 68
def f1(n):
    if(n==0) : return 5
    else : return f1(n-1) + n*7
#max 32
def f2(n):
    if(n==0) : return 1
    elif(n==1) : return 2
    else : return 2*f2(n-1) - f2(n-2) + n
n = int(input())
sum = 0
nothing = 0
for _ in range(n):
    number = int(input())
    if((number <=68) & (number%2==0)) : sum += f1(number)
    elif((number <=32) & (number%2==1)) : sum += f2(number)
    elif(number%3==0) : sum+= number**2
    else : nothing += 1
print(sum%101)
print(nothing)