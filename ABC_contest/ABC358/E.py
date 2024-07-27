import sys
from collections import deque,defaultdict
import itertools
import heapq
import bisect
import queue
from scipy.special import comb,perm

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

K = ii()
C = li()

#Combを階乗の乗法の逆元で計算する
#K!までをフェルマーの小定理を使って求める（mod 998244353）

#fact: n!の値
fact = [1] * (K+1)
for i in range(K):
    fact[i+1] = fact[i] * (i+1) % mod
#ifact: n!の逆元の値
ifact = [1] * (K+1)
ifact[K] = pow(fact[K],mod-2,mod)
for i in range(K,0,-1):
    ifact[i-1] = ifact[i] * i % mod

def c(n,r):
    #n! / r!(n-r)!
    return fact[n] * ifact[r] % mod * ifact[n-r] % mod


dp = [[0] * (K+1) for _ in range(27)]
dp[0][0] = 1

#iがC[i]番目、i番目の文字をK文字並べりゅ
#jが前の参照箇所。ひとつ前のiのK文字全列挙したパターンを取得する
#kが並べる作業。
for i in range(26):
    for j in range(K+1):
        for k in range(min(C[i],K-j) + 1):
            dp[i+1][j+k] += dp[i][j] * c(j+k,k) % mod
            dp[i+1][j+k] %= mod

print(sum(dp[-1][1:]) % mod)