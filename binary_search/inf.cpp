#include <bits/stdc++.h>
#define forn(i,a,b) for (int i = a; i < b; i++)
using namespace std;

int bin_search(int x, vector<int>& a);

int main()
    {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        int N, K; cin >> N >> K;
        vector<int> arr1(N), arr2(K);
        forn(i,0,N)
           cin >> arr1[i];
        forn(i,0,K)
           cin >> arr2[i];

        forn(i,0,K)
            cout << arr1[bin_search(arr2[i], arr1)] << endl;
        return 0;
    }
int bin_search(int x, vector<int>& A)
    {
        int n = A.size(), l = -1, r = A.size();
        if (n == 1)
            return 0;
        while (l+1 < r)
        {
            int m = (l+r)/2;
            if (A[m] == x) return m;
            if (A[m] < x) l = m;
            else r = m;
        }
        if (!r) return 0;
        return (((0 < r) && (r < n)) && ((abs(A[r] - x) < abs(A[r-1] - x))))?r:r-1;
    }
