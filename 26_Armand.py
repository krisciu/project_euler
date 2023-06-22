longest_chain = ""
longest_length = 0
longest_dum = 1
for target in range(3, 1000):
    remainder_list = []
    remainder_set = set()
    remainder = 1
    chain = ""
    while True:
        if remainder in remainder_set:
            chain_length = 0
            i = len(remainder_list)
            while remainder_list[i-1] != remainder:
                chain_length = chain_length + 1
                i = i - 1
                chain = chain + str(remainder_list[i-1])
            if chain_length > longest_length:
                longest_length = chain_length
                longest_chain = chain
                longest_dum = target
            break

        remainder_list.append(remainder)
        remainder_set.add(remainder)

        remainder *= 10
        aux = remainder // target
        remainder = remainder % target

print(longest_chain)
print(longest_length)
print(longest_dum)

