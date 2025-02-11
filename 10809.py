s = input()
alpa = [-1] * 26
for i in range(len(s)):
    idx = ord(s[i])-97
    if alpa[idx] == -1:
        alpa[idx] = i
print(" ".join(map(str, alpa)))
