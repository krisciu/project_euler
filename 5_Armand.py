last = 1
for t in range(2, 20):
    i = 0
    while True:
        i = i + 1
        if i % last == 0 and i % t == 0:
            last = i
            break
print(last)

