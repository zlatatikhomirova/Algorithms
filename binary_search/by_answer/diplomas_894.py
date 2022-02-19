from numpy.random import randint as rand

def lbinsearch(l, r, check, checkparams):
    while (l < r):
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def checkm(m, params):
    w, h, n = params
    return (m // w) * (m // h) >= n
    
def CHECKlbinsearch(w, n, h):
    m = 0
    while (m // w) * (m // h) < n:
        m += 1
    return m

def sampleTest():
    w, h, n = map(int, "2 3 10".split())  
    assert lbinsearch(0, (w if w >= h else h) * n, checkm, (w, h, n)) == 9
    assert lbinsearch(0, (w if w >= h else h) * n, checkm, (w, h, n)) == CHECKlbinsearch(w, n, h)
    w, h, n = map(int, "1 1 1".split())  
    assert lbinsearch(0, (w if w >= h else h) * n, checkm, (w, h, n)) == 1
    assert lbinsearch(0, (w if w >= h else h) * n, checkm, (w, h, n)) == CHECKlbinsearch(w, n, h)
    
def stress(w, h, n):
    ans1 = lbinsearch(0, (w if w >= h else h) * n, checkm, (w, h, n))
    ans2 = CHECKlbinsearch(w, n, h)
    return (ans1, ans2, ans1 == ans2)

def genTest():
    lowBoundWHN, upBoundWHN = map(int, (1, 1e2))
    W, H, N = rand(lowBoundWHN, upBoundWHN, 3)
    ans1, ans2, ans = stress(W, H, N) 
    assert ans == True, f"W {W} H {H} N {N}\nans1Lbin = {ans1}\nans2Check = {ans2}"

sampleTest()
    
for i in range(10):
    genTest()

print("Done!")

"""
Final solution:

def lbinsearch(l, r, check, checkparams):
    while (l < r):
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def checkm(m, params):
    w, h, n = params
    return (m // w) * (m // h) >= n    

w, h, n = map(int, input().split()) 
print(lbinsearch(0, (w if w >= h else h) * n, checkm, (w, h, n)))
"""
