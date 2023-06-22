num = 999999
prime = [True for i in range(num + 1)]
p = 2
while (p * p <= num):

    # If prime[p] is not
    # changed, then it is a prime
    if (prime[p] == True):

        # Updating all multiples of p
        for i in range(p * p, num + 1, p):
            prime[i] = False
    p += 1

coefficient_range = 1000
longest_prime_chain = 0
longest_prime_chain_a = coefficient_range * -1 - 1
longest_prime_chain_b = coefficient_range * -1 - 1
for a in range(coefficient_range * -1, coefficient_range + 1):
    for b in range(coefficient_range * -1, coefficient_range + 1):
        n = 0
        while True:
            res = n * n + a * n + b
            if not prime[res]:
                break
            n = n + 1
        if n > longest_prime_chain:
            longest_prime_chain = n
            longest_prime_chain_a = a
            longest_prime_chain_b = b
print(longest_prime_chain)
print("a: " + str(longest_prime_chain_a))
print("b: " + str(longest_prime_chain_b))
