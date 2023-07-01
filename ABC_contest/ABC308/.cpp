#include <bits/stdc++.h>
typedef long long ll;
const int INF = 1e9;
const ll LINF = 1e18;
using namespace std;

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
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define revrep(i, n) for (int i = n; i >= 0; i--)
#define rrep(i, n) for (int i = 1; i <= (int)(n); i++)
#define bit(k) (1LL << (k))
#define all(x) (x).begin(), (x).end()

void print_multiset(std::multiset<int>& ms) {
    for (auto val: ms) {
        std::cout << val << ", ";
    }
    std::cout << std::endl;
}

int main(){
    int N;
    cin >> N;
    multiset<ll> check;

    rep(i,N){
        ll a,b,num;
        cin >> a >> b;
        num = a / (a+b);
        check.insert((num,i+1));
    }

    
    return 0;
}
