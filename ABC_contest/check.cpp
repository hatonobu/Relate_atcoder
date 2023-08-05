#include <bits/stdc++.h>
typedef long long ll;
const int INF = 1e9;
const ll LINF = 1e18;
using namespace std;
 
/*
  　　∧_∧
　（ ´・ω・)
　 //＼￣￣旦＼   @author mn01137
／/ ※ ＼＿＿＿＼
＼＼ 　※ 　※ 　※ ヽ
　 ＼ヽ-＿_＿--＿__ヽ
*/
 
/*---------------- template  -------------------------*/
 
template <class T>
bool clamp(T x, T min, T max) { return (x >= min and x <= max); }
template <class T>
void chmin(T &a, const T &b)
{
    if (b < a)
        a = b;
}
template <class T>
void chmax(T &a, const T &b)
{
    if (a < b)
        a = b;
}
 
// int dx[4] = {1, 0, -1, 0};
// int dy[4] = {0, 1, 0, -1};
 
/*---------------- macro -------------------------*/
 
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define revrep(i, n) for (int i = n; i >= 0; i--)
#define rrep(i, n) for (int i = 1; i <= (int)(n); i++)
#define bit(k) (1LL << (k))
#define all(x) (x).begin(), (x).end()
#define fill(x, y) memset(x, y, sizeof(x))
#define UNIQUE(v) v.erase(unique(v.begin(), v.end()), v.end());
 
/*-------------- source code --------------------*/
 
int mex(vector<int> x, int k)
{
    cout << k << endl;
    while (x[k] != 0)
    {
        k++;
    }
    cout << k << endl;
    
    return k;
}
 
void solve()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<int> a, b;
    rep(i, s.size())
    {
        if (s[i] == 'A')
        {
            a.push_back(i);
        }
        else
        {
            b.push_back(i);
        }
    }
    vector<int> x(200009, 0);
    int ai = a.size();
    int bi = b.size();
    int aidx = 0, bidx = 0;
    int k = 0;
    rrep(i, n)
    {
        if (i % 2 == 0)
        {
            // bobの行動
            if (aidx < ai)
            {
                x[a[aidx]] = 1;
                aidx++;
            }
        }
        else
        {
            // aliceの行動
            if (bidx < bi)
            {
                x[b[bidx]] = 1;
                bidx++;
            }
        }
        k = mex(x, k);
        if (s[k] == 'A')
        {
            cout << "Alice" << endl;
        }
        else
        {
            cout << "Bob" << endl;
        }
    }
}

int main()
{
    // cout << fixed << setprecision(10);
    cin.tie(0)->sync_with_stdio(0);
    solve();
}