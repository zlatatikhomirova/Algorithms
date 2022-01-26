#include <bits/stdc++.h>
#define forn(i,a,b) for (int i = a; i < b; i++)
using namespace std;
void evc(int a, int b, int c, int d);
int main()
    {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        
        int N;
        cin >> N;
        forn(i, 0, N)
            {
                int a, b; cin >> a >> b;
                int c, d; cin >> c >> d;
                evc(a, b, c, d);}
        return 0;
    }
    
void evc(int a, int b, int c, int d){
    while (b){
                    if((a == c) && (b == d)){
                        cout << "YES" << endl;
                        return;
                    }
                    if (b>a) swap(a, b);
                    a -= b;
                }
        cout << "NO" << endl;
        return;
}
