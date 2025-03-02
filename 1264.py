result = []
while True:
    count = 0
    case = input()
    if case == "#":
        break
    for char in case:
        if char in 'AEIOUaeiou':
            count += 1
    result.append(count)
print(*result, sep="\n")