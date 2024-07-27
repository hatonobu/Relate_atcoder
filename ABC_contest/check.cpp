#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

const long long MOD = 998244353;
const long long INF = 8 * 1000000000000000000LL;

bool check(const string &s, int k) {
    for (int i = 0; i <= s.size() - k; ++i) {
        string t = s.substr(i, k);
        string rt = t;
        reverse(rt.begin(), rt.end());
        if (t == rt) {
            return false;
        }
    }
    return true;
}

int main() {
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    set<string> check_set;
    int ans = 0;

    sort(S.begin(), S.end());
    do {
        if (check(S, K)) {
            ans += 1;
            check_set.insert(S);
        }
    } while (next_permutation(S.begin(), S.end()));

    cout << ans << endl;

    return 0;
}
