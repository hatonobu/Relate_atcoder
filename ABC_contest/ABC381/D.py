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
A = li()

def check(N):
    ans = 0
    now = 0
    setList = set()
    q = deque()
    for i in range(N // 2):
        if A[2*i] == A[2*i + 1]:
            if A[2*i] in setList:
                while(q):
                   num = q.popleft()
                   setList.remove(num)
                   now -= 1
                   if num == A[2*i]:
                       break
                   
            now += 1
            q.append(A[2*i])
            setList.add(A[2*i])
        else:
            setList.clear()
            now = 0
        
        ans = max(ans,now)
    
    return 2*ans

def check2(N):
    ans = 0
    now = 0
    setList = set()
    q = deque()
    for i in range((N-1) // 2):
        #print(i)
        if A[2*i+1] == A[2*i + 2]:
            if A[2*i + 1] in setList:
                while(q):
                   num = q.popleft()
                   setList.remove(num)
                   now -= 1
                   if num == A[2*i + 1]:
                       break
                   
            now += 1
            q.append(A[2*i + 1])
            setList.add(A[2*i + 1])
        else:
            setList.clear()
            now = 0
        
        ans = max(ans,now)
    
    return 2*ans
answer = 0

answer = max(answer,check(N))
#print(answer)
answer = max(answer,check2(N))  
#print(answer)
          
print(answer)     