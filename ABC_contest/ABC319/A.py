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
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

S = input()
d = {"tourist" :3858,"ksun48" :3679,"Benq" :3658,"Um_nik" :3648,"apiad": 3638,"Stonefeang": 3630,"ecnerwala" :3613,"mnbvmar" :3555,"newbiedmy" :3516,"semiexp" :3481}

print(d[S])