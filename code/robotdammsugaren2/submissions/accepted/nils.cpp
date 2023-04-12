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

void remark(pt p){
    if(grid[p.x][p.y] != 2)return;
    dust--;
    grid[p.x][p.y] = 0;
    row_sum[p.x].update(p.y, 1);
    col_sum[p.y].update(p.x, 1);
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

vector<pt> make_move_save(int d){
    vector<pt> res;
    while(1){
        if(grid[now.x][now.y] == 0)res.push_back(now);
        unmark(now);
        if(toint(now) == nxt[now.x][now.y][d])break;
        now.x += DX[d];
        now.y += DY[d];
    }
    return res;
}

int par_dir[MAXN*MAXN+MAXN] = {0};
int parent[MAXN*MAXN+MAXN] = {0};
int steps[MAXN*MAXN+MAXN] = {0};
int seen[MAXN*MAXN+MAXN] = {0};
int sum[MAXN*MAXN+MAXN] = {0};
int bfs_counter = 0;
vector<int> visited;

void bfs(int max_dist, int min_x){
    max_dist = min(max_dist, k-sz(answer));
    visited.clear();
    bfs_counter++;
    queue<int> Q;
    Q.push(toint(now));
    seen[toint(now)] = bfs_counter;
    sum[toint(now)] = 0;
    steps[toint(now)] = 0;
    parent[toint(now)] = -1;
    visited.push_back(toint(start));
    while(!Q.empty()){
        int a = Q.front();
        Q.pop();
        if(steps[a] >= max_dist)continue;
        if(topt(a).x < min_x)continue;
        rep(d,0,4){
            int w = dist(topt(a), d);
            int b = nxt[a/m][a%m][d];
            if(seen[b] != bfs_counter){
                seen[b] = bfs_counter;
                steps[b] = steps[a]+1;
                sum[b] = -1;
                visited.push_back(b);
                Q.push(b);
            }
            if(steps[b] == steps[a]+1){
                if(sum[b] < sum[a]+w){
                    sum[b] = sum[a]+w;
                    parent[b] = a;
                    par_dir[b] = d;
                }
            }
        }
    }
}

void bfs_move(int max_dist, int min_x=-1, bool max_sum=0){
    bfs(max_dist, min_x);
    double best = -1;
    int goal = -1;
    trav(i, visited){
        if(steps[i] > 0 && steps[i] <= k-sz(answer)){
            double temp = double(sum[i]) / double(steps[i]);
            if(max_sum)temp = sum[i];
            if(temp > best){
                best = temp;
                goal = i;
            }
        }
    }
    vector<int> moves;
    while(parent[goal] != -1){
        moves.push_back(par_dir[goal]);
        goal = parent[goal];
    }
    reverse(all(moves));
    trav(d, moves){
        make_move(d);
    }
}

pair<int,int> tree_search(int depth){
    if(depth == 0)return {dust,0};
    int ans = dust;
    int best_dir = -1;
    rep(d,0,4){
        if(dist2(now, d) > 0){
            if(best_dir == -1)best_dir = d;
            pt old = now;
            vector<pt> marks = make_move_save(d);
            int temp = tree_search(depth-1).first;
            if(temp > ans || (temp == ans && rand()%2==0)){
                ans = temp;
                best_dir = d;
            }
            trav(p, marks){
                remark(p);
            }
            now = old;
        }
    }
    return {ans, best_dir};
}

void solve_tree_search(int depth, int bfs_save = 10){
    while(sz(answer) < k){
        pair<int,int> res = tree_search(min(depth, k-sz(answer)));
        if(res.first == dust){
            bfs_move(bfs_save);
            continue;
        }
        make_move(res.second);
    }
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

    if(T == 0){
        solve_tree_search(10);
    }
    if(T == 1){
        solve_tree_search(10);
    }
    if(T == 2){
        solve_tree_search(10);
    }
    if(T == 3){
        solve_tree_search(10, 100);
    }
    if(T == 4){
        solve_tree_search(10, 100);
    }
    if(T == 5){
        solve_tree_search(7);
    }
    if(T == 6){
        while(sz(answer) < k){
            bfs_move(100);
        }
    }
    if(T == 7){
        bfs_move(k);
        while(sz(answer) < k){
            bfs_move(20);
        }
    }
    if(T == 8){
        while(sz(answer) < k){
            bfs_move(20);
        }
    }
    if(T == 9){
        solve_tree_search(9);
    }

    if(T == 10){
        bfs_move(k);
        while(sz(answer) < k){
            bfs_move(100, 700);
        }
    }

    /*
    rep(c1,0,n){
        rep(c2,0,m){
            if(grid[c1][c2] == 1)cout << "#";
            if(grid[c1][c2] == 0)cout << " ";
            if(grid[c1][c2] == 2)cout << "O";
        }cout << "\n";
    }
    */
    cout << answer << "\n";
    cerr << T << ": " << dust << "\n";
    return 0;
}
