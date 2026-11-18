import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    smallest_diff = float('inf')

    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        if diff < smallest_diff:
            smallest_diff = diff

    if smallest_diff < 0:
        print(0)
    else:
        print((smallest_diff // 2) + 1)

t = int(input())
for i in range(t):
    solution()
