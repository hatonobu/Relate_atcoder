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
INF = 8 * 10**18

A,B,C,D = mi()
ans = 0
#横4,縦1 = 2cm (*1倍)
tate = D - B
yoko = C - A
while(A < C):
    #print(ans)
    if yoko % 4 == 0:
        ans += (yoko // 4) * tate * 2 * 2
        break
    else:
        check = A % 4
        #print(check)
        if check == 0:
            lis = [2,1]
            if D % 2 != B % 2:
                ans += lis[(B % 2)]
                ans += ((tate-1) // 2) * 3
            else:
                ans += (tate // 2) * 3
        elif check == 1:
            lis = [1,2]
            if D % 2 != B % 2:
                ans += lis[(B % 2)]
                ans += ((tate-1) // 2) * 3
            else:
                ans += (tate // 2 )* 3
        elif check == 2:
            lis = [0,1]
            if D % 2 != B % 2:
                ans += lis[(B % 2)]
                ans += (tate-1) // 2
            else:
                ans += tate // 2
        else:  
            lis = [1,0]
            if D % 2 != B % 2:
                ans += lis[(B % 2)]
                ans += (tate-1) // 2
            else:
                ans += tate // 2
        A += 1
        yoko -= 1

print(ans)
        