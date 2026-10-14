#include <bits/stdc++.h>
using namespace std;

vector<long long> ask(long long k) {
    cout << "? " << k << endl;
    long long q;
    if (!(cin >> q)) exit(0);
    if (q == -1) exit(0);
    if (q == 0) return {};
    vector<long long> path(q);
    for (int i = 0; i < q; i++) cin >> path[i];
    return path;
}

void solve() {
    long long n;
    if (!(cin >> n)) return;

    long long MAX_PATHS = (1LL << 30);
    vector<long long> starts(n + 2);
    starts[1] = 1;

    for (int u = 1; u <= n; u++) {
        vector<long long> check = ask(starts[u] + 1);
        if (check.empty() || check[0] > u) {
            starts[u + 1] = starts[u] + 1;
            continue;
        }

        long long L = starts[u] + 2;
        long long R = MAX_PATHS;
        long long ans = R + 1;

        while (L <= R) {
            long long mid = L + (R - L) / 2;
            vector<long long> path = ask(mid);
            if (path.empty() || path[0] > u) {
                ans = mid;
                R = mid - 1;
            } else {
                L = mid + 1;
            }
        }
        starts[u + 1] = ans;
    }

    vector<long long> count(n + 1);
    for (int u = 1; u <= n; u++) {
        count[u] = starts[u + 1] - starts[u];
    }

    vector<pair<int, int>> edges;
    for (int u = 1; u <= n; u++) {
        long long curr = starts[u] + 1;
        long long limit = starts[u + 1];
        while (curr < limit) {
            vector<long long> path = ask(curr);
            if (path.size() < 2) {
                curr++;
                continue;
            }
            edges.push_back({u, (int)path[1]});
            curr += count[path[1]];
        }
    }

    cout << "! " << edges.size();
    for (auto &e : edges) {
        cout << "\n" << e.first << " " << e.second;
    }
    cout << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}