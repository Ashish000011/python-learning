import sys
input = sys.stdin.readline

def solution():
    
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    
    for  item in a:
        if (item >= a[k-1] and item > 0 ):
            count += 1
        else:
            continue
    print(count)

solution()