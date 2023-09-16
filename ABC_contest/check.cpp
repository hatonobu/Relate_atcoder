#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rrep(i, n) for (int i = 1; i <= (int)(n); i++)
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define mod 998244353

template <class T>
bool clamp(T x, T min, T max) { return (x >= min and x <= max); }
template <class T>
void chmin(T &a, const T &b) noexcept
{
    if (b < a)
        a = b;
}
template <class T>
void chmax(T &a, const T &b) noexcept
{
    if (a < b)
        a = b;
}


template <class T>
void print(vector<T> &a)
{
    for (auto nx : a)
        cout << nx << ' ';
    cout << endl;
}

int main() {
    // code
    int n,d,p;
    cin >> n >> d >> p;
    vector<ll> f(n+d);
    rep(i,n){
        cin >> f[i];
    }
    sort(rall(f));
    ll cnt=0;
    ll sum=0;
    for(int i = 0;i<d;i++){
        sum += f[i];
        //cout << i << ',' << sum << endl;
        if(i == d-1 and sum > p){
            i=0;
            sum = 0;
            cnt++;
            f.erase(f.begin(),f.begin()+d);
        }
        else{

        }
    }

    print(f);
    //cout << cnt << endl;
    //if(cnt>=1)f.erase(f.begin(),f.begin()+d*cnt);
    ll ans = 0;
    for(int i =0;i < n;i++){
        //cout <<  << endl;
        ans += f[i];
    }
    cout << ans+p*cnt << endl;
    return 0;
}
