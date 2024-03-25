x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
if x1 == x2:
    if x2 == x3:
        print('infinity')
    else:
        print('not comparable')
elif x2 == x3:
    print('not comparable')
else:
    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y3 - y2) / (x3 - x2)
    if m1 == m2:
        print(m1)
    elif m1 > m2:
        print(m1 - m2)
    else:
        print(m2 - m1)
