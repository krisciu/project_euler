lo = 2
hi = 9999999
mega_total = 0
for i in range(lo, hi + 1):
    total = 0
    current = i
    while current != 0:
        total += (current % 10) ** 5
        current //= 10
    if total == i:
        mega_total += total
        print(total)
print(mega_total)
