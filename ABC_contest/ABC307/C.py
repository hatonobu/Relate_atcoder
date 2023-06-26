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
lli = lambda n: [li() for _ in range(n)]
mod = 998244353

H,W = mi()
A = [input() for _ in range(H)]

H2,W2 = mi()
B = [input() for _ in range(H2)]

Hx,Wx = mi()
X = [input() for _ in range(Hx)]

def get_black(h,w,lis):
    return_lis = []
    for i in range(h):
        for j in range(w):
            if lis[i][j] == "#":
                return_lis.append((i,j))
    
    return return_lis

lis_A = get_black(H,W,A)
lis_B = get_black(H2,W2,B)
lis_X = set(get_black(Hx,Wx,X))

for i in range(-10,10):
    for j in range(-10,10):
        for k in range(-10,10):
            for l in range(-10,10):
                check = set()
                for x,y in lis_A:
                    check.add((x+i,y+j))
                for x,y in lis_B:
                    check.add((x+k,y+l))
                if check == lis_X:
                    print("Yes")
                    exit()

print("No")