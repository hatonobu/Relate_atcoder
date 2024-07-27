#Combを階乗の乗法の逆元で計算する
#K!までをフェルマーの小定理を使って求める（mod 998244353）
K = 1000
mod = 998244353

#fact: n!の値
fact = [1] * (K+1)
for i in range(K):
    fact[i+1] = fact[i] * (i+1) % mod
#ifact: n!の逆元の値
ifact = [1] * (K+1)
ifact[K] = pow(fact[K],mod-2,mod)
for i in range(K,0,-1):
    ifact[i-1] = ifact*i % mod

def c(n,r):
    #n! / r!(n-r)!
    return fact[n] * ifact[r] % mod * ifact[n-r] % mod