word = input()
cnt = [0] * 26
for i in range(len(word)):
    cnt[ord(word[i]) - ord('a')] += 1

print(' '.join(map(str, cnt)))