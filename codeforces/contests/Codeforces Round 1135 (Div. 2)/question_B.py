"""
B. Diverse String
time limit per test1.5 seconds
memory limit per test256 megabytes

The diversity of a binary string s
 is the number of distinct∗
 strings that can be obtained by performing the following operation at most once:

Choose an integer 0≤x≤1
 and two integers 1≤l≤r≤n
, and set si:=x
 for all l≤i≤r
.

For example, the string 10 has diversity 3
 because the strings 10, 11, and 00. can be obtained.

You are given a string s
 of length n
 as well as an integer k
. You are allowed to toggle the values of at most k
 characters in the string. Your task is to determine the maximum possible diversity of the resulting string.

∗
Two strings a
 and b
 are distinct if there exists an index i
 such that ai≠bi
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each test case contains two integers n
 and k
 (1≤n≤2⋅105
, 0≤k≤n
) — the length of the string and the maximum number of characters you are allowed to toggle.

The second line of each test case contains a binary string s
 of length n
.

It is guaranteed that the sum of n
 over all test cases does not exceed 3⋅105
.

Output
For each test case, output a line with a single integer — the maximum possible diversity of the string after toggling at most k
 characters.

Example
InputCopy
4
1 1
0
4 4
1001
5 1
11111
7 2
1101001
OutputCopy
2
11
16
23
Note
In the first test case, it is optimal to toggle the first character, resulting in the string 1 with a diversity of 2
.

In the second test case, the string 1111 achieves the maximum possible diversity of 11
.


"""


def solve(n, k, s):
    ones = s.count("1")
    zeros = n - ones

    big = max(ones, zeros)
    small = min(ones, zeros)

    change = min(k, small)
    big = big + change
    small = small - change

    answer = 1 + big * (big + 1) // 2 + small * (small + 1) // 2
    print(answer)


t = int(input())
for x in range(t):
    line = input().split()
    n = int(line[0])
    k = int(line[1])
    s = input()
    solve(n, k, s)