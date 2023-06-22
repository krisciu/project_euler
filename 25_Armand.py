left = 1
right = 1
n = 3
while True:
    fib = left + right
    if len(str(fib)) >= 1000:
        break
    left = right
    right = fib
    n = n + 1
print(n)
print(right)
