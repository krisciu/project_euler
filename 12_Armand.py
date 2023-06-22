from functools import reduce


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


j = 1
while True:
    tn = int(j * (j + 1) / 2)
    if len(factors(tn)) > 500:
        print(tn)
        break
    j = j + 1
