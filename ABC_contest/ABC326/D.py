import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

N = ii()
R = input()
C = input()

def print_lis(lis):
    for i in lis:
        print("".join(i))

def check_yoko(lis):
    for i in range(N):
        for j in range(N):
            if lis[i][j] == ".":
                pass
            elif lis[i][j] == R[i]:
                break
            else:
                return False
    return True

def check_tate(lis):
    for i in range(N):
        for j in range(N):
            if lis[j][i] == ".":
                pass
            elif lis[j][i] == C[i]:
                break
            else:
                return False
    return True

def make_lis(a,b,c,d,e):
    pass


                    


