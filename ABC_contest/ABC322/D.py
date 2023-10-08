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

def rot_left90(S):
    return list(zip(*S[::-1]))

A = [input() for _ in range(4)]
B = [input() for _ in range(4)]
C = [input() for _ in range(4)]
total = 0
for i in range(4):
    for j in range(4):
        total += (A[i][j] == "#") + (B[i][j] == "#") + (C[i][j] == "#")
if total != 16:
    print("No")
    exit()


def check(A,B,C,ax,ay,bx,by,cx,cy):
    for y in range(4):
        for x in range(4):
            num = 0
            if 0 <= x+ax < 4 and 0 <= y+ay < 4:
                if A[y+ay][x+ax] == "#":
                    num += 1
            if 0 <= x+bx < 4 and 0 <= y+by < 4:
                if B[y+by][x+bx] == "#":
                    num += 1
            if 0 <= x+cx < 4 and 0 <= y+cy < 4:
                if C[y+cy][x+cx] == "#":
                    num += 1
            if num != 1:
                return False
    return True

def print_lis(lis):
    for i in lis:
        print(i)
    print("==================")

def shift_check(A,B,C):
    ax,ay = 0,0
    bx,by = 0,0
    cx,cy = 0,0
    for i in range(-3,4):
        ay = i
        for j in range(-3,4):
            ax = j
            for k in range(-3,4):
                by = k
                for l in range(-3,4):
                    bx = l
                    for m in range(-3,4):
                        cy = m
                        for n in range(-3,4):
                            cx = n
                            if check(A,B,C,ax,ay,bx,by,cx,cy):
                                print("Yes")
                                exit()

for i in range(4):
    A = rot_left90(A)
    for j in range(4):
        B = rot_left90(B)
        for k in range(4):
            C = rot_left90(C)
            shift_check(A,B,C)

print("No")
        
            