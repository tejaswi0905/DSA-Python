#include <bits/stdc++.h>
using namespace std;
#define int long long

// find with path compression on unordered_map 'par'.
// If x is not present in par, then x is its own representative (we return x).
int find_rep(unordered_map<int,int> &par, int x) {
    auto it = par.find(x);
    if (it == par.end()) return x;         // not present -> representative is itself

    // path compression (iterative)
    // collect path
    vector<int> path;
    int cur = x;
    while (true) {
        auto jt = par.find(cur);
        if (jt == par.end()) break;
        path.push_back(cur);
        int nxt = jt->second;
        if (nxt == cur) break;
        cur = nxt;
    }
    int rep = cur;
    // compress
    for (int node : path) par[node] = rep;
    return rep;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (!(cin >> T)) return 0;
    while (T--) {
        int n;
        cin >> n;

        // store portals: each portal is expected to be 4 integers (l r a b)
        vector<array<int,4>> portals;
        portals.reserve(n);
        for (int i = 0; i < n; ++i) {
            int l, r, a, b;
            cin >> l >> r >> a >> b;
            portals.push_back({l, r, a, b});
        }

        int q;
        cin >> q;
        vector<int> queries(q);
        for (int i = 0; i < q; ++i) cin >> queries[i];

        // mapping similar to Python's defaultdict(int) named 'par'
        unordered_map<int,int> par;
        par.reserve(1024);

        // Apply the same logic as the Python code:
        // For each portal (l,r,a,b) the python code iterates num in [l..b]
        // and sets par[num] = max(par[num], b) (or par[num]=b if absent).
        for (auto &pr : portals) {
            int l = pr[0], /*r = pr[1],*/ /*a = pr[2],*/ b = pr[3];
            for (int num = l; num <= b; ++num) {
                auto it = par.find(num);
                if (it == par.end()) par[num] = b;
                else if (b > it->second) it->second = b;
            }
        }

        // answer queries using find with path compression
        vector<int> ans;
        ans.reserve(q);
        for (int x : queries) {
            int rep = find_rep(par, x);
            ans.push_back(rep);
        }

        // print results
        for (size_t i = 0; i < ans.size(); ++i) {
            if (i) cout << ' ';
            cout << ans[i];
        }
        cout << '\n';
    }

    return 0;
}
