# answer of q 2_2
# by Omid Heydari

a = int(input())
b = int(input())
c = int(input())

if a + b <= c or a + c <= b or b + c <= a:
    print(1)
elif c * c + b * b == a * a or b * b + a * a == c * c or c * c + a * a == b * b:
    print(4)
elif a == b or b == c or a == c:
    print(3)
else:
    print(2)
