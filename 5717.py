friends = []
while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0:
        break
    friends.append(M + F)

for i in friends:
    print(i)