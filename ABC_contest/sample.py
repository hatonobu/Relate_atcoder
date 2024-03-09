import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import math

#sys.setrecursionlimit(10 ** 9)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
ml = lambda: map(str, input().split())
li = lambda: list(mi())
li_st = lambda: list(map(str, input().split()))
lli = lambda n: [li() for _ in range(n)]
mod = 998244353
INF = 10**18

import random
import time
d = defaultdict(int)

def roulette_spin(name_lis):
    return random.randint(0, len(name_lis)*100) % len(name_lis)

name_lis = ["zannen","Eightask","kumamama","parly","かずき","とある暇人","東京に行けます","プリキュア+2","Valo+2","top-1","次の人ポイント0!!!!"]
random.shuffle(name_lis)
random.shuffle(name_lis)
random.shuffle(name_lis)
random.shuffle(name_lis)
#print(name_lis)

#ルーレットを回転させて結果を表示
result = roulette_spin(name_lis)
print(f"ルーレットの結果:")
print("prprprprprprprprprprprprprprpr")
time.sleep(3)
print("でーーーーーん！！！！！")
time.sleep(1)
print(name_lis[result])
