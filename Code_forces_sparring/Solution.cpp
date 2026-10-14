#include <bits/stdc++.h>
using namespace std;

// ====================================================
//                CONFIGURATION
// ====================================================
// Set to true to run stress tests.
// Set to false to submit to the online judge.
const bool TESTING_MODE = true; 

// ====================================================
//                THE JUDGE (Test Generator)
// ====================================================
namespace Judge {
    int N;
    vector<vector<int>> adj;
    vector<vector<int>> all_paths;
    set<pair<int, int>> hidden_edges;
    set<pair<int, int>> reported_edges;
    int queries_used;

    // Generates a random Directed Acyclic Graph
    void generate_case() {
        N = rand() % 10 + 2; // Random N between 2 and 11
        adj.assign(N + 1, vector<int>());
        hidden_edges.clear();
        all_paths.clear();
        reported_edges.clear();
        queries_used = 0;

        // Create random edges (u < v ensures no cycles)
        for (int u = 1; u <= N; ++u) {
            for (int v = u + 1; v <= N; ++v) {
                if (rand() % 2) { // 50% chance of edge
                    adj[u].push_back(v);
                    hidden_edges.insert({u, v});
                }
            }
        }
    }

    // DFS to find all lexicographically sorted paths
    void build_paths() {
        for (int i = 1; i <= N; ++i) sort(adj[i].begin(), adj[i].end());

        function<void(int, vector<int>&)> dfs = [&](int u, vector<int>& p) {
            p.push_back(u);
            all_paths.push_back(p);
            for (int v : adj[u]) {
                dfs(v, p);
            }
            p.pop_back();
        };

        vector<int> current_path;
        for (int i = 1; i <= N; ++i) {
            dfs(i, current_path);
        }
        sort(all_paths.begin(), all_paths.end());
    }

    // Mock response to "? k"
    vector<long long> query(long long k) {
        queries_used++;
        if (k < 1 || k > all_paths.size()) return {};
        
        // Convert int vector to long long vector for compatibility
        vector<int>& p = all_paths[k - 1];
        vector<long long> res(p.begin(), p.end());
        return res;
    }

    // Check if the user's answer matches the hidden graph
    bool verify() {
        return reported_edges == hidden_edges;
    }
}

// ====================================================
//                YOUR SOLUTION
// ====================================================

// Modified ask function to switch between Judge and Real Interaction
vector<long long> ask(long long k) {
    if (TESTING_MODE) {
        return Judge::query(k);
    } else {
        cout << "? " << k << endl;
        long long q;
        if (!(cin >> q)) exit(0);
        if (q == -1) exit(0);
        if (q == 0) return {};
        vector<long long> path(q);
        for (long long i = 0; i < q; i++) cin >> path[i];
        return path;
    }
}

void solve() {
    long long n;
    
    if (TESTING_MODE) {
        n = Judge::N; // Get N from Judge
    } else {
        if (!(cin >> n)) return;
    }

    long long MAX_PATHS = (1LL << 30); 

    vector<long long> starts(n + 2);
    starts[1] = 1;

    // STEP 1: Binary Search
    for (long long u = 1; u <= n; u++) {
        long long L = starts[u] + 1;
        long long R = MAX_PATHS;        
        long long ans = R + 1;

        while (L <= R) {
            long long mid = L + (R - L) / 2;
            vector<long long> path = ask(mid);

            bool is_next_block = false;
            if (path.empty() || path[0] > u) is_next_block = true;

            if (is_next_block) {
                ans = mid;
                R = mid - 1;
            } else {
                L = mid + 1;
            }
        }
        starts[u + 1] = ans;
    }

    // STEP 2: Counts
    vector<long long> count(n + 1);
    for (long long u = 1; u <= n; u++)
        count[u] = starts[u + 1] - starts[u];

    // STEP 3: Find Edges
    vector<pair<long long, long long>> edges;
    for (long long u = 1; u <= n; u++) {
        long long curr = starts[u] + 1;
        long long limit = starts[u + 1];

        while (curr < limit) {
            vector<long long> path = ask(curr);
            
            if (path.size() < 2) {
                curr++;
                continue;
            }

            long long v = path[1];
            edges.push_back({u, v});
            curr += count[v];
        }
    }

    // OUTPUT / VERIFY
    if (TESTING_MODE) {
        for (auto& e : edges) {
            Judge::reported_edges.insert({(int)e.first, (int)e.second});
        }
    } else {
        cout << "! " << edges.size();
        for (auto &e : edges)
            cout << "\n" << e.first << " " << e.second;
        cout << endl;
    }
}

// ====================================================
//                MAIN DRIVER
// ====================================================
int main() {
    srand(time(0)); 

    if (TESTING_MODE) {
        cout << "--- STARTING STRESS TEST (1000 Runs) ---" << endl;
        for (int i = 1; i <= 1000; ++i) {
            Judge::generate_case();
            Judge::build_paths();
            
            solve();
            
            if (Judge::verify()) {
                if (i % 100 == 0) cout << "Test " << i << " Passed ✅" << endl;
            } else {
                cout << "❌ FAILED on Test " << i << endl;
                cout << "N = " << Judge::N << endl;
                cout << "Hidden Edges:" << endl;
                for(auto p : Judge::hidden_edges) cout << p.first << "->" << p.second << " ";
                cout << "\nYour Edges:" << endl;
                for(auto p : Judge::reported_edges) cout << p.first << "->" << p.second << " ";
                cout << endl;
                return 1;
            }
        }
        cout << "🎉 ALL TESTS PASSED!" << endl;
    } 
    else {
        // Normal Submission Mode
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        long long t;
        if (cin >> t) {
            while (t--) {
                solve();
            }
        }
    }
    return 0;
}