import sys
from collections import Counter

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().strip().split()))

counter = Counter(cards)

M = int(input().strip())

queries = list(map(int, input().strip().split()))

results = [counter[query] for query in queries]
print(' '.join(map(str, results)))
