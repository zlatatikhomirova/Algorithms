from numpy.random import randint as rand

def LBinS(A, x, n):
    l, r = -1, n
    while (r>l+1):
        m = (l+r)//2
        if A[m] == x:
            a, b = [m]*2
            while A[b] == x:
                b -= 1
            b+=2
            while a < n and A[a] == x:
                a += 1
            return b, a
        if A[m] < x:
            l = m
        else:
            r = m
    return 0

def CHECKLBinS(A, x, n):
    a, i = 0, 0
    while i < n:
        if A[i] == x:
            a = i
            while i < n and A[i] == x:
                i += 1
            return a, i-1
        i += 1
    return 0

def genTest():
    upBoundNK, lowBoundNK = 2*1e4, 1
    upBoundAB, lowBoundAB = 1e9+1, -1e9
    N, K = rand(lowBoundNK, upBoundNK, 2)
    A = sorted(rand(lowBoundAB, upBoundAB, N))
    B = rand(lowBoundAB, upBoundAB, K)
    assert stress(N, A, B) == True, f"{N}\n{A}\n{B}"
    
def stress(N, A, B):
    ans1 = []
    for x in B:
        ans1.append(LBinS(A, x, N))
    print("ANS1 RECEIVED.")
    ans2 = []
    for x in B:
        ans2.append(CHECKLBinS(A, x, N))
    print("ANS2 RECEIVED.")
    return ans1 == ans2

for i in range(10):
    genTest()
print("Done!")

"""
Final solution:

N, M = [int(i) for i in input().split()] 
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
for e in B:
    try:
        print(*LBinS(e, N))
    except TypeError:
        print(0)
"""
