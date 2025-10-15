#include <bits/stdc++.h>
using namespace std;

#define mxn 200005
#define ll long long
ll val[] = {1, 10, 100, 1000, 10000};
ll dp[mxn][7][2], n;
string s;

ll solve(int in, int mx, int changed) {
    if (in == 1) {
        return 0;
    }
    if (dp[in][mx][changed] != -1) {
        return dp[in][mx][changed];
    }
    int sign = 1;
    if (s[in] - 'A' < mx) {
        sign = -1;
    }
    ll res = sign * val[s[in] - 'A']+solve(in - 1, max(mx, int(s[in] - 'A')), changed);
    if (!changed) {
        for (int i = 0; i < 5; i++) {
            if (i != s[in] - 'A') {
                sign = 1;
                if (i < mx) {
                    sign = -1;
                }
                res = max(res, sign*val[i] + solve(in - 1, max(mx, i), 1));
            }
        }
    }

    dp[in][mx][changed] = res;
    return res;
}


int main() {
    int t;
    cin >> t;
    while (t--) {
        cin >> s;
        n = s.size();
        memset(dp, -1, sizeof(dp[0]) * (n + 1));
        ll ans = solve(n - 1, 0, 0);
        cout << ans << "\n";
    }
}