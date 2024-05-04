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

N,H,W = mi()
AB = lli(N)


def emb(sx,sy,x,y,lis,total):
    f = True
    r_total = total
    back_lis = []
    for h in range(sy,sy+y):
        if f == False:
            break
        for w in range(sx,sx+x):
            if w < 0 or w >= W or h < 0 or h >= H:
                f = False
                break
            else:
                if lis[h][w] == 0:
                    lis[h][w] = 1
                    r_total += 1
                    back_lis.append([h,w])
                else:
                    f = False
                    break

    if f:
        return True, r_total
    else:
        for h,w in back_lis:
            lis[h][w] = 0
        return False, total
    

for e2 in itertools.permutations(range(N)):
    for e in itertools.product(range(2),repeat=N):
        ans = [[0]*W for _ in range(H)]
        total = 0
        for num in e2:
            if e[num] == 0:
                x,y = AB[num]
            else:
                y,x = AB[num]

            check = False
            for dy in range(H):
                if check == True:
                    break
                for dx in range(W):
                    if ans[dy][dx] == 0:
                        flag, total = emb(dx,dy,x,y,ans,total)
                        check = True
                        break
            
            if flag:
                if total == H*W:
                    #print(ans)
                    print("Yes")
                    exit()
            else:
                break
        

print("No")