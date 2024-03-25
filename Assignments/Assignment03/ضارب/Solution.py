inp = input()

inputs = inp.split(" ")
start = int(inputs[0])
end = int(inputs[1])

product = 1

for i in range(start + 1, end):
    product *= i

print(product)