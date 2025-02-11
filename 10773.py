K = int(input())
numbers = []
for i in range(K):
    num = int(input())
    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)
print(sum(numbers))