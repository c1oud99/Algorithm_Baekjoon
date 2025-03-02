result = []
while True:
    case = input()
    if case == "#":
        break
    result.append(sum(1 for char in case if char in 'AEIOUaeiou'))
print(*result, sep="\n")