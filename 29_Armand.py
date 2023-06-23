start = 2
threshold = 100

distinct = set()
for a in range(start, threshold + 1):
    for b in range(start, threshold + 1):
        distinct.add(pow(a, b))
print(len(distinct))