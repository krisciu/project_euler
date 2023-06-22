abundant_list = []
abundant_set = set()
for i in range(1, 28123):
    sum_divisors = 0
    for j in range(1, i):
        if i % j == 0:
            sum_divisors += j
    if sum_divisors > i:
        abundant_list.append(i)
        abundant_set.add(i)


def can_be_two_abundant(target):
    for abundant in abundant_list:
        if (target - abundant) in abundant_set:
            return True
    return False


sum_non_abundant = 0
for i in range(1, 28124):
    if not can_be_two_abundant(i):
        sum_non_abundant += i
print(sum_non_abundant)
