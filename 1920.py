N = int(input())
A_list = list(map(int, input().split()))
A_list.sort()

M = int(input())
M_val = list(map(int, input().split()))

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if(data[mid] == target):
            return 1
        elif(data[mid] > target):
            end = mid - 1
        elif(data[mid] < target):
            start = mid + 1
    return 0

for target in M_val:
    print(binary_search(target, A_list))