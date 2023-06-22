sums_to_nums = {}
nums_to_sums = {}
for i in range(1, 10000):
    divisor_sum = 0
    for j in range(1, i):
        if i % j == 0:
            divisor_sum = divisor_sum + j
    nums_to_sums[i] = divisor_sum
total_sum = 0
for i in range(1, 10000):
    s = nums_to_sums[i]
    if i != s and s in nums_to_sums and nums_to_sums[s] == i:
        total_sum += i
print(total_sum)
