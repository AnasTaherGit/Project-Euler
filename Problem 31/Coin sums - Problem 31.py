target = 200
CoinSize = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * 201

ways[0] = 1

for i in range(0, len(CoinSize)):
    for j in range(CoinSize[i], target + 1):
        ways[j] += ways[j - CoinSize[i]]

print(ways[-1])
