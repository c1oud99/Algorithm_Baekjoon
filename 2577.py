ABC = str(int(input()) * int(input()) * int(input()))
count = []
for i in range(10):
    count.append(ABC.count(str(i)))

print('\n'.join(str(cnt) for cnt in count))