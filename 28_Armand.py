res = 1
jump = 2
cur = 1
width = 1001
for i in range(0, width // 2):
    res = res + 4 * cur + 10 * jump
    cur = cur + 4 * jump
    jump = jump + 2
print(res)
