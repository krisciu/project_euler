import math
res = ""
permutations = math.factorial(10)
target = 999999
available = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(10, 0, -1):
    permutations /= i
    cur = math.floor(target / permutations)
    target = target % permutations
    res = res + str(available[cur])
    available.remove(available[cur])
print(res)
