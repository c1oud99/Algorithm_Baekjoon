import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]

arr.sort()

for i in arr:
    print(i)