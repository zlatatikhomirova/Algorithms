from numpy.random import randint as rand

def lbinsearch(l, r, A, x):
    while l < r:
        m = (l + r) // 2
        if A[m] == x:
            return "YES"
        if A[m] > x:
            r = m
        else:
            l = m + 1
    return "NO"

def CHECKlbinsearch(A, x):
    if x in A:
        return "YES"
    else:
        return "NO"
    
def genTest():
    upBoundNK, lowBoundNK = 1e5, 1
    upBoundAB, lowBoundAB = 1e9+1, -1e9
    N, K = rand(lowBoundNK, upBoundNK, 2)
    A = sorted(rand(lowBoundAB, upBoundAB, N))
    B = sorted(rand(lowBoundAB, upBoundAB, K))
    assert stress(N, A, B) == True, f"{N}\n{A}\n{B}"
    
def stress(N, A, B):
    ans1 = ""
    for x in B:
        ans1 += lbinsearch(-1, N, A, x)
    print("ANS1 RECEIVED.")
    ans2 = ""
    for x in B:
        ans2 += CHECKlbinsearch(A, x)
        print("Step")
    print("ANS2 RECEIVED.")
    return ans1 == ans2

for i in range(10):
    genTest()
print("Done!")

"""
Final solution:
    
N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

for x in B:
    print(lbinsearch(-1, N, x))
"""
