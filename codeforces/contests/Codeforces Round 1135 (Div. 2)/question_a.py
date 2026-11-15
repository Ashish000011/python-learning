""" A. Composite Permutation
time limit per test1 second
memory limit per test256 megabytes

You are given an integer n
. Construct a permutation∗
 p
 of length n
 such that i⋅pi
 is composite†
 for every 1≤i≤n
, or determine that no such permutation exists.

∗
A permutation of length n
 is an array consisting of n
 distinct integers from 1
 to n
 in arbitrary order. For example, [2,3,1,5,4]
 is a permutation, but [1,2,2]
 is not a permutation (2
 appears twice in the array), and [1,3,4]
 is also not a permutation (n=3
 but there is 4
 in the array).

†
A positive integer x
 is composite if it has at least one other divisor besides 1
 and x
. For example, 6
 is composite because 2
 is a divisor of it, while 1
 and 5
 are not.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). The description of the test cases follows.

The only line of each test case contains a single integer n
 (1≤n≤100
).

Output
For each test case, if no suitable permutation exists, print a single integer −1
.

Otherwise, print n
 integers p1,p2,…,pn
 representing a suitable permutation.

If there are multiple solutions, print any of them.

Example
InputCopy
3
1
4
5
OutputCopy
-1
4 3 2 1
4 5 3 1 2
Note
In the first test case, it can be shown that no suitable permutation exists.

In the second test case, the values of i⋅pi
 are 4
, 6
, 6
, and 4
, respectively, which are all composite. """


def composite_permutation(n):
    if n < 4:
        print(-1)
    else:
        print(4, 2, 3, 1, end="")
        for i in range(5, n + 1):
            print("1",i, end="")
        print()


t = int(input())
for x in range(t):
    n = int(input())
    composite_permutation(n)