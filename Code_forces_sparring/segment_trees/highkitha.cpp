#include <bits/stdc++.h>
using namespace std;

#define ll long long

// ------------------ SEGMENT TREE CLASS ------------------
class SegmentTree {
public:
    int n;
    vector<int> tree;

    SegmentTree(int size) {
        n = size;
        tree.assign(4 * n, 0);
    }

    void build(vector<int> &arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return;
        }
        int mid = (start + end) / 2;
        build(arr, 2 * node + 1, start, mid);
        build(arr, 2 * node + 2, mid + 1, end);
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }

    void update(int idx, int val, int node, int start, int end) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid)
            update(idx, val, 2 * node + 1, start, mid);
        else
            update(idx, val, 2 * node + 2, mid + 1, end);
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    }

    int query(int l, int r, int node, int start, int end) {
        if (r < start || l > end)
            return 0;
        if (l <= start && end <= r)
            return tree[node];
        int mid = (start + end) / 2;
        int left = query(l, r, 2 * node + 1, start, mid);
        int right = query(l, r, 2 * node + 2, mid + 1, end);
        return left + right;
    }
};

// ------------------ MAIN SOLUTION ------------------
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    cin >> n >> m >> q;
    string s;
    cin >> s;

    vector<pair<int, int>> ranges(m);
    for (int i = 0; i < m; i++) cin >> ranges[i].first >> ranges[i].second;

    vector<int> priority(n + 1, 0);
    set<int> remaining;
    for (int i = 1; i <= n; i++) remaining.insert(i);

    int nextPriority = 0, d = 0;
    for (auto [l, r] : ranges) {
        while (true) {
            auto it = remaining.lower_bound(l);
            if (it == remaining.end() || *it > r) break;
            priority[*it] = nextPriority++;
            remaining.erase(it);
            d++;
        }
    }

    for (int x : remaining) priority[x] = nextPriority++;

    vector<int> arr(nextPriority, 0);
    int totalOnes = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '1') {
            arr[priority[i + 1]] = 1;
            totalOnes++;
        }
    }

    SegmentTree seg(nextPriority);
    seg.build(arr, 0, 0, nextPriority - 1);

    while (q--) {
        int idx;
        cin >> idx;
        idx--; // make 0-indexed for string

        if (s[idx] == '1') {
            s[idx] = '0';
            totalOnes--;
            seg.update(priority[idx + 1], 0, 0, 0, nextPriority - 1);
        } else {
            s[idx] = '1';
            totalOnes++;
            seg.update(priority[idx + 1], 1, 0, 0, nextPriority - 1);
        }

        int count = min(d, totalOnes);
        int onesInPriority = 0;
        if (count > 0)
            onesInPriority = seg.query(0, count - 1, 0, 0, nextPriority - 1);

        cout << (count - onesInPriority) << "\n";
    }

    return 0;
}
