#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
using i128 = __int128;

bool check(int64 n) {
    for (int p = 2; p <= 60; ++p) {
        int64 lo = 2, hi = 1e6;
        while (lo <= hi) {
            int64 mid = (lo + hi) / 2;
            i128 total = 1, term = 1;
            for (int i = 0; i < p; ++i) {
                term *= mid;
                total += term;
                if (total > n) break;
            }
            if (total == n) return true;
            if (total < n) lo = mid + 1;
            else hi = mid - 1;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        long long n; cin >> n;
        cout << (check(n) ? "YES\n" : "NO\n");
    }
}
