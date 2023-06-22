digits = ['one', 'two',   'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
          'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty',
          'sixty', 'seventy', 'eighty', 'ninety']
counts = {}
joined = digits + teens
for i in range(len(joined)):
    counts[i+1] = len(joined[i])
for i in range(len(tens)):
    p = len(tens[i])
    counts[(i + 2) * 10] = p      # e.g. twenty
    for j in range(len(digits)):
        counts[(i + 2) * 10 + (j + 1)] = p + len(digits[j])
for i in range(0, 9):
    p = counts[i+1] + len("hundred")
    counts[(i + 1) * 100] = p
    for j in range(1, 100):
        counts[(i + 1) * 100 + j] = p + len("and") + counts[j]
for i in range(0, 9):
    p = counts[i+1] + len("thousand")
    counts[(i + 1) * 1000] = p
    for j in range(1, 1000):
        counts[(i + 1) * 1000 + j] = p + counts[j]

count_sum = 0
for i in range(1, 1001):
    count_sum = count_sum + counts[i]

print(count_sum)
