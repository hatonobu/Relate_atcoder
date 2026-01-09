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

N,M = mi()
XYZ = lli(M)

check = [[0]* 60 for _ in range(N)]
for x,y,z in XYZ:
    #zを2進数に変換
    z_bin = format(z,"060b")
    #yにzの該当するようにbitを立てて、xに対応箇所を負の値で格納
    #yに該当の通りbitが立てられない場合、対応箇所が負の値で一致→入れ替える
    for i in range(60):
        if z_bin[i] == "1":
            if check[y-1][i] == 0:
                check[y-1][i] = x
            else:
                num = check[y-1][i] * -1
                if num == INF:
                    print(-1)
                    exit()
                check[num][i] = -y
                check[y-1][i] = -INF
            check[x-1][i] = -y
        else:
            pass

for i in range(N):
    lis = []
    for j in range(60-1,-1,-1):
        ans = 0
        if check[i][j] > 0:
            ans += 2**j
    lis.append(ans)

print(*lis)