import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    x = 0

    for _ in range(n):
        a = input().strip().upper()

        if a == "++X" or a == "X++":
            x += 1

        elif a == "--X" or a == "X--":
            x -= 1

    print(x)

solution()