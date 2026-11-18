import sys
input = sys.stdin.readline

def solution():
    m , n = map(int, input().split())
    total = m*n

    
    ans = total//2
    print(ans)

solution()
