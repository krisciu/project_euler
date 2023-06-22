ssq = 0
sqs = 0
for i in range(1, 101):
    ssq = ssq + i * i
    sqs = sqs + i
sqs = sqs * sqs
print(ssq)
print(sqs)
print(sqs - ssq)