#include<bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;
const long long LINF = 1e18;
const long long MOD1000000007 = 1000000007;
const long long MOD998244353 = 998244353;
typedef long long ll;
typedef vector<int> vii;
typedef vector<ll> vll;
#define rrep(i, n) for (int i = 1; i <= (int)(n); i++)
#define rep(i, n) for (int i = 0;i < (int)(n); i++)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mod 998244353

int dx[] = { 1,0,-1,0,1,1,-1,-1 };
int dy[] = { 0,1,0,-1,1,-1,1,-1 };

template <class T>
bool clamp(T x, T min, T max) { return (x >= min && x <= max); }
template <class T>
void chmin(T &a, const T &b) noexcept {
    if (b < a) a = b;
}
template <class T>
void chmax(T &a, const T &b) noexcept {
    if (a < b) a = b;
}

int main() {
    // code
    int n;
    cin >> n;
    string s[n];
    rep(i,n){
        cin >> s[i];
    }

    int m = 0;
    rep(i,n){
        int S = s[i].size();
        chmax(m,S);
    }
    rep(i,n){
        if(s[i].size() < m){
            rep(j,m-s[i].size()){
                s[i].push_back('*');
            }
        }
    }
    string t[m];
    rep(i,m){
        rep(j,n){
            //cout << s[n-j-1][i] << endl;
            if(s[n-j-1][i] == '*'){
                t[i].push_back('*');    
            }
            else{
                t[i].push_back(s[n-j-1][i]);
            }
        }
    }
    rep(i,m){
        rep(j,n){
            if(t[i].back() == '*' || t[i].back() == ' '){
                t[i].pop_back();
            }
        }
        
    }
    for(auto x : t){
        cout << x << endl;
        cout << x.size() << endl;
    }
    return 0;
}