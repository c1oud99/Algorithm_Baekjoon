num = []
for i in range(28):
    num.append(int(input()))

num.sort()
for i in range(1, 31):
    if i not in num:
        print(i)