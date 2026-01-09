import sys
from collections import deque,defaultdict
#import pypyjit
import itertools
import heapq
import bisect
import queue

#pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 8 * 10**18

S = input()

stack = []


for s in S:
    if len(stack) == 0:
        stack.append(s)
    else:
        if s == ")":
            if stack[-1] == "(":
                stack.pop()
        elif s == "]":
            if stack[-1] == "[":
                stack.pop()
        elif s == ">":
            if stack[-1] == "<":
                stack.pop()
        else:
            stack.append(s)


if len(stack) == 0:
    print("Yes")
else:
    print("No")