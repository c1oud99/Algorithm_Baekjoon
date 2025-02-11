N = int(input())
list = []
result = []

for i in range(N):
    list.append(input())

list.sort()
list.sort(key = len)

for word in list:
    if word not in result:
        result.append(word)

for word in result:
    print(word)