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

N = ii()
H = li()

st = [10000000]

ans = []
for i in range(N-1,0,-1):
    num = H[i]
    while(True):
        if st[-1] < num:
            st.pop()
        else:
            break
    st.append(num)
    ans.append(len(st)-1)

print(*ans[::-1] + [0])