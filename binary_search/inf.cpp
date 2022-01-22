#include <bits/stdc++.h>
#define forn(i,a,b) for (int i = a; i < b; i++)
using namespace std;

int bin_search(int x, int L, int R, vector<int>& a);

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
        {
            int R = bin_search(arr2[i], 0, N-1, arr1);
            cout << arr1[R] << endl;
        }
        return 0;
    }
int bin_search(int x, int L, int R, vector<int>& a)
    {
        int left, right, m;
        left = L; right = R;
        while (right - left > 1)
        {
            m = (right + left) / 2;
            if (a[m] == x)
                return m;
            if (a[m] < x) left = m;
            else right = m;
        }
    return right-1;
    }
