#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;

struct FT {
	vector<ll> s;
	FT(int n) : s(n) {}
	void update(int pos, ll dif) { // a[pos] += dif
		for (; pos < sz(s); pos |= pos + 1) s[pos] += dif;
	}
	ll query(int pos) { // sum of values in [0, pos)
		ll res = 0;
		for (; pos > 0; pos &= pos - 1) res += s[pos-1];
		return res;
	}
};

struct pt{
    int x,y;
};

int const MAXN = 2001;
int T,n,m,k;

pt start, now;
int grid[MAXN][MAXN] = {0};
string dir = "v^><";
int DX[4] = {1,-1,0,0};
int DY[4] = {0,0,1,-1};
string answer = "";
int dust = 0;

int nxt[MAXN][MAXN][4] = {0};
vector<FT> row_sum(MAXN, FT(MAXN));
vector<FT> col_sum(MAXN, FT(MAXN));

int toint(pt p){
    return p.x*m+p.y;
}

pt topt(int i){
    return {i/m,i%m};
}

void precomp(){
    rep(c1,0,n){
        int prev = -1;
        rep(c2,0,m){
            if(grid[c1][c2] == 0){
                if(prev == -1)prev = c1*m+c2;
                nxt[c1][c2][3] = prev;
            }
            else{
                prev = -1;
            }
        }
        for(int c2 = m-1; c2 >= 0; c2--){
            if(grid[c1][c2] == 0){
                if(prev == -1)prev = c1*m+c2;
                nxt[c1][c2][2] = prev;
            }
            else{
                prev = -1;
            }
        }
    }

    rep(c2,0,m){
        int prev = -1;
        rep(c1,0,n){
            if(grid[c1][c2] == 0){
                if(prev == -1)prev = c1*m+c2;
                nxt[c1][c2][1] = prev;
            }
            else{
                prev = -1;
            }
        }
        for(int c1 = n-1; c1 >= 0; c1--){
            if(grid[c1][c2] == 0){
                if(prev == -1)prev = c1*m+c2;
                nxt[c1][c2][0] = prev;
            }
            else{
                prev = -1;
            }
        }
    }
    rep(c1,0,n){
        rep(c2,0,m){
            if(grid[c1][c2] == 0){
                row_sum[c1].update(c2,1);
                col_sum[c2].update(c1,1);
            }
        }
    }
}

void unmark(pt p){
    if(grid[p.x][p.y] != 0)return;
    dust++;
    grid[p.x][p.y] = 2;
    row_sum[p.x].update(p.y, -1);
    col_sum[p.y].update(p.x, -1);
}

// Amount of dust
int dist(pt p, int d){
    pt q = topt(nxt[p.x][p.y][d]);
    int res;
    if(d == 0)res = col_sum[p.y].query(q.x+1) - col_sum[p.y].query(p.x+1);
    if(d == 1)res = col_sum[p.y].query(p.x) - col_sum[p.y].query(q.x);
    if(d == 2)res = row_sum[p.x].query(q.y+1) - row_sum[p.x].query(p.y+1);
    if(d == 3)res = row_sum[p.x].query(p.y) - row_sum[p.x].query(q.y);
    return res;
}

// Manhattan distance
int dist2(pt p, int d){
    pt q = topt(nxt[p.x][p.y][d]);
    return abs(p.x-q.x) + abs(p.y-q.y);
}

void make_move(int d){
    answer += dir[d];
    while(toint(now) != nxt[now.x][now.y][d]){
        unmark(now);
        now.x += DX[d];
        now.y += DY[d];
    }unmark(now);
}

int main() {

    cin >> T >> n >> m >> k;
    rep(c1,0,n){
        string line;
        cin >> line;
        rep(c2,0,m){
            grid[c1][c2] = (line[c2] == '#');
            if(line[c2] == 'O')start = {c1,c2};
        }
    }
    precomp();
    now = start;

    rep(c1,0,k){
        int best_dir = -1;
        int best = -1;
        rep(c2,0,4){
            int d = dist(now, c2);
            if((d > best || (d == best && rand()%2 == 0)) && dist2(now, c2) != 0){
                best = d;
                best_dir = c2;
            }

        }
        make_move(best_dir);
    }

    cout << answer << "\n";
    return 0;
}
