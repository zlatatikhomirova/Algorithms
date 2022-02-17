from numpy.random import randint as rand

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l
def checkisgt(index, params):
    seq, x = params
    return seq[index] > x

def checkisge(index, params):
    seq, x = params
    return seq[index] >= x

def findfirst(seq, x, check):
    ans = lbinsearch(0, len(seq)-1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def res(seq, x):
    indexgt = findfirst(seq, x, checkisgt)
    indexge = findfirst(seq, x, checkisge)
    if seq[indexgt-1] != x:
        return 0
    return indexge + 1, indexgt

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

def minTest():
    N, K = 1, 1
    A = [1]
    B = [1]
    assert stress(N, A, B) == True, f"{N}\n{A}\n{B}"
    
def maxTest():
    N, K = map(int, (2*1e4, 2*1e4))
    upBoundAB, lowBoundAB = map(int, (1e9+1, -1e9))
    A = sorted(rand(lowBoundAB, upBoundAB, N))
    B = rand(lowBoundAB, upBoundAB, K)
    assert stress(N, A, B) == True, f"{N}\n{A}\n{B}"
    
def sampleTest():
    N, K = 10, 5
    A = [int(i) for i in "1 1 3 3 5 7 9 18 18 57".split()]
    B = [int(i) for i in "57 3 9 1 179".split()]
    assert stress(N, A, B) == True, f"{N}\n{A}\n{B}"
    
def genTest():
    upBoundNK, lowBoundNK = map(int, (2*1e1, 1))
    upBoundAB, lowBoundAB = map(int, (1e2+1, -1e2))
    N, K = rand(lowBoundNK, upBoundNK, 2)
    A = sorted(rand(lowBoundAB, upBoundAB, N))
    B = rand(lowBoundAB, upBoundAB, K)
    assert stress(N, A, B) == True, f"{N}\n{A}\n{B}"
    
def stress(N, A, B):
    ans1 = ""
    print("A:\n", A, "\nB:\n", B)
    for x in B:
        a = res(A, x)
        if a:
            ans1 += f"{a[0]} {a[1]}\n"
        else:
            ans1 += f"{a}\n"
    print("ANS1 RECEIVED.")
    print("ANS1:\n", ans1)
    ans2 = ""
    for x in B:
        ans = CHECKLBinS(A, x, N)
        if not ans:
            ans2 += "0\n"
        else:
            ans2 += f"{ans[0]+1} {ans[1]+1}\n"
    print("ANS2 RECEIVED.")
    print("ANS2:\n", ans2)
    print()
    return ans1 == ans2
sampleTest()

for i in range(100):
    genTest()
minTest()
maxTest()
print("Done!")

"""
Final solution:

N, M = [int(i) for i in input().split()] 
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
for x in B:
    a = res(A, x)
    if a:
        print(*a)
    else:
        print(0)
"""
