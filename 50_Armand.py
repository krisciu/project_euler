threshold = 1000000
primes = []
prime_lookup = [True for i in range(threshold + 1)]
# sieve
p = 2
while (p * p <= threshold):
    if (prime_lookup[p] == True):
        for i in range(p * p, threshold + 1, p):
            prime_lookup[i] = False
    p += 1
for p in range(2, threshold + 1):
    if prime_lookup[p] and p <= threshold:
        primes.append(p)
longest_chain = 0
longest_chain_prime = 0
for i in range(len(primes)):
    cum_sum = 0
    for j in range(i, len(primes)):
        cum_sum = cum_sum + primes[j]
        if cum_sum > threshold:
            break
        if prime_lookup[cum_sum] and j - i > longest_chain:
            longest_chain = j - i
            longest_chain_prime = cum_sum

print(longest_chain)
print(longest_chain_prime)


