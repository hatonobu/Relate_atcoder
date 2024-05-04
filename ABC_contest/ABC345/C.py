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

def can_cover_all_tiles(H, W, N, tiles):
    def can_place_tile(grid, i, j, a, b):
        for x in range(i, i + a):
            for y in range(j, j + b):
                if x >= H or y >= W or grid[x][y] == 0:
                    return False
        return True

    def place_tile(grid, i, j, a, b):
        for x in range(i, i + a):
            for y in range(j, j + b):
                grid[x][y] = 0

    grid = [[1] * W for _ in range(H)]

    for tile in tiles:
        placed = False
        for i in range(H):
            for j in range(W):
                if can_place_tile(grid, i, j, tile[0], tile[1]):
                    place_tile(grid, i, j, tile[0], tile[1])
                    placed = True
                    break
            if placed:
                break
        if not placed:
            return False

    return True

# 入力の取得
N,H,W = map(int, input().split())
tiles = [tuple(map(int, input().split())) for _ in range(N)]

# タイル配置が可能か判定
result = can_cover_all_tiles(H, W, N, tiles)
if result:
    print("Yes")
else:
    print("No")
