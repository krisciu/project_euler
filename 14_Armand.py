chain_lengths = {1: 1}


def collapse(n, cur_len):
    if n in chain_lengths:
        return cur_len + chain_lengths[n]
    if n % 2 == 0:
        return collapse(n / 2, cur_len + 1)
    return collapse(3 * n + 1, cur_len + 1)


max_length = 0
for i in range(1, 1000000):
    length = collapse(i, 0)
    if length > max_length:
        max_length = length
    chain_lengths[i] = length
print(max(chain_lengths, key=chain_lengths.get))
