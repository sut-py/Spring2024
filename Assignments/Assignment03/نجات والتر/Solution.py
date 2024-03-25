
def digits_sum(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n /= 10
    return sum_digit


def change_base(decimal_number, k):
    answer = 0
    exponent = 0
    while decimal_number > 0:
        remainder = decimal_number % k
        answer += remainder * (10 ** exponent)
        exponent += 1
        decimal_number = decimal_number // k

    return answer


first_line = list(map(int, input().split()))
n = first_line[0]
m = first_line[1]
k = int(input())

maximum = 0
ans = n
for i in range(min(n, m+1), max(n, m+1)):
    if digits_sum(change_base(i, k)) > maximum:
        maximum = digits_sum(change_base(i, k))
        ans = i

print(ans)
