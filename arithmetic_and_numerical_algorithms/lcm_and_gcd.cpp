#include <bits/stdc++.h>
using namespace std;

int lcm (int, int);
int gcd (int, int);

int main()
    {
        ios::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
    
        return 0;
    }

int gcd (int a, int b) {
	while (b) {
		a %= b;
		swap (a, b);
	}
	return a;
}

int lcm (int a, int b) {
  int c = a, d = b.
  while (b) {
		a %= b;
		swap (a, b);
	}
	return c / a * d;
}
