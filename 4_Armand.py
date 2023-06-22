import math
m = 0
# for i in range(999, 99, -1):
#     for j in range(99, 9, -1):
#         p = i * j
#         print(p)
#         if int(p / 1000) == p / 100 and (p % 100) == (p / 100):
#             m = math.max(p, max)
#         if int(p / 1000) == p / 1000 and (p % 1000) == (p / 1000):
#             m = math.max(p, max)
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        p = i * j
        ps = str(p)
        # if int(p / 100) == p / 100 and (p % 100) == (p / 100):
        #     m = math.max(p, max)
        if ps[0:3] == ps[3:6][::-1]:
            if p > m:
                m = p
print(m)
