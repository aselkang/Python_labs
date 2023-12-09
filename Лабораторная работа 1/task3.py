players = list(map(str, input().split()))
k = len(players)
players1 = players[:k//2]
players2 = players[k//2:(k-k%2)]
print(players1)
print(players2)