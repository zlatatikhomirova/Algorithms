int bin_search(int x, L, R) 
    { 
        int left, right, m; 
        left = L; right = R; 
        while (right - left > 1) 
        { 
            m = (right + left) / 2; 
            if (a[m] < x) left = m; 
            else right = m; 
        } 
    return right; 
    }
while (l<r) {
m=(l+r)/2;
if (a[m]<k) l=m+1;
else r=m;
}
if (a[r]==k) printf("%d", r);
else printf("-1");

r = x;
l = 1;
while (fabs(l-r)>eps) {
m=(l+r)/2;
if (m*m*m<x) l=m;
else r=m;
}

int main(void)
{
int n, x, y, i, j, l, r, now;
double speed;
scanf("%d%d%d", &n, &i, &j);
x=i<j?i:j;
y=i>j?i:j;
l=0;
r = (n-1)*y;
while (l != r) {
now = (l+r)/2;
j = now / x + now / y;
if (j < n-1) l = now+1;
else r = now;
}
printf("%d", r+x);
return 0;
}




int BinarySearch(int val, vector<int>& A)
{
    int left = 0, right = A.size() - 1, index = -1;
    while ((left <= right) && (index == -1))
    {
        int middle = (left + right) / 2;
        if (A[middle] == val) index = middle;
        else
        {
            if (val < A[middle]) right = middle - 1
            else left = middle + 1;
        }
    }
    return index;
    }
