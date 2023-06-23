coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins_value = dict()
coins_value[0] = set()
coins_value[0].add((0, 0, 0, 0, 0, 0, 0, 0))
for i in range(1, 201):
    coins_value[i] = set()
    for coin_idx, coin in enumerate(coins):
        if i - coin >= 0:
            for prev_coins in coins_value[i - coin]:
                new_coins = list(prev_coins)
                new_coins[coin_idx] += 1
                coins_value[i].add(tuple(new_coins))
print(coins_value[200])
print(len(coins_value[200]))

