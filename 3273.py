n = int(input())
num = list(map(int, input().split()))
x = int(input())
num.sort()
cnt, start = 0, 0
end = n - 1

while start < end:
    compare = num[start] + num[end]
    if compare == x:
        cnt += 1
        start += 1
        end -= 1
    elif compare < x:
        start += 1
    else: # compare > x
        end -= 1

print(cnt)