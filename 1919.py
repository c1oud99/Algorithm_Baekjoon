from collections import Counter
first = input()
second = input()
cnt_first = Counter(first)
cnt_second = Counter(second)
count_diff = (cnt_first - cnt_second) + (cnt_second - cnt_first)
print(sum(count_diff.values()))