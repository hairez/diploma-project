#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(i, a) for(auto& i : a)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


struct FT {
  vector<int> s;
  FT(int n) : s(n) {}
  void update(int pos, int dif) { // a[pos] += dif
    for (; pos < sz(s); pos |= pos + 1) s[pos] += dif;
  }
  int query(int pos) { // sum of values in [0, pos)
    int res = 0;
    for (; pos > 0; pos &= pos - 1) res += s[pos-1];
    return res;
  }
  int query(int low, int hi) { // sum of values in [low, hi]
    return query(hi+1)-query(low);
  }
};

const int dx[] = {-1,0,1,0};
const int dy[] = {0,1,0,-1};

int main() {
  int START_TIME = clock();
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);
  int tc,n,m,k;
  cin >> tc >> n >> m >> k;
  vector<string> grid(n);
  rep(i,0,n) cin>>grid[i];
  int KK = k;

  auto at = [&](int x, int y) { return x + n*y; };
  auto X = [&](int q) { return q%n; };
  auto Y = [&](int q) { return q/n; };
  int N = at(n,m);

  vector<FT> row_fw;
  vector<FT> col_fw;
  vi cleaned;

  auto clean = [&](int x, int y) {
    if(cleaned[at(x,y)]) return;
    cleaned[at(x,y)] = 1;
    row_fw[x].update(y,-1);
    col_fw[y].update(x,-1);
  };

  auto reset = [&](){
    row_fw = vector<FT>(n,m);
    col_fw = vector<FT>(m,n);
    cleaned = vi(N,0);
    rep(x,0,n) rep(y,0,m) {
      row_fw[x].update(y,1);
      col_fw[y].update(x,1);
    }
    k = KK;
  };

  auto dist = [&](int q1, int q2) {
    int x0 = X(q1), x1 = X(q2);
    int y0 = Y(q1), y1 = Y(q2);
    if(x0 > x1) swap(x0,x1);
    if(y0 > y1) swap(y0,y1);
    if(x0 == x1) return row_fw[x0].query(y0,y1);
    if(y0 == y1) return col_fw[y0].query(x0,x1);
    assert(false);
  };
  auto clean_path = [&](int q1, int q2) {
    int x0 = X(q1), x1 = X(q2);
    int y0 = Y(q1), y1 = Y(q2);
    if(x0 > x1) swap(x0,x1);
    if(y0 > y1) swap(y0,y1);
    rep(x,x0,x1+1) rep(y,y0,y1+1) clean(x,y);
  };

  vector<vi> nxt(4,vi(N,-1));
  vi bad(N,1);

  int start = -1;
  rep(x,0,n) rep(y,0,m) if(grid[x][y] == 'O')
    start = at(x,y);

  { // init nxt
    rep(x,0,n) rep(y,0,m) if(grid[x][y] != '#') {
      bad[at(x,y)] = 0;
      rep(d,0,4) {
        nxt[d][at(x,y)] = at(x,y);
        int nx = x + dx[d], ny = y + dy[d];
        if(grid[nx][ny] != '#')
          nxt[d][at(x,y)] = at(nx,ny);
      }
    }
    function<int(int,int)> go = [&](int q, int d) {
      assert(!bad[q]);
      if(nxt[d][q] == q) return q;
      return nxt[d][q] = go(nxt[d][q],d);
    };
    rep(d,0,4) rep(q,0,N) if(!bad[q]) go(q,d);
  }

  auto go = [&](int depth, int start) { // brute force search next few moves
    pair<int,vi> best = {-1,{}};
    vi pth;
    function<void(int,int,int,int)> search = [&](int x, int depth, int len, int dir) {
      pth.emplace_back(x);
      if(depth == 0) {
        if(best.first == len && rand()%2) best = {len, pth};
        if(best.first < len) best = {len, pth};
        pth.pop_back();
        return;
      }
      rep(d,0,4) if((dir-d+4)%4 != 2)
        search(nxt[d][x], depth-1, len + dist(x,nxt[d][x]), d);
      pth.pop_back();
    };
    search(start, depth, 0, rand()%4);
    assert(best.first != -1);
    return best.second;
  };


  pair<int,vi> best;
  vi try_s = {1,2,3,4,8,8,8,8,9};
  bool cont = true;
  while(cont) for(int s: try_s) {
    if(clock()-START_TIME > 4.9*CLOCKS_PER_SEC) {
      cont = false;
      break;
    }

    reset();

    vi path;
    path.emplace_back(start);
    while(k > 0) {
      int dep = min(k,s);
      k -= dep;
      vi gogo = go(dep, path.back());
      path.insert(path.end(), 1+all(gogo));
      rep(i,0,sz(gogo)-1) clean_path(gogo[i], gogo[i+1]);
    }
    assert(sz(path) == KK+1);
    int c = count(all(cleaned),1);
    best = max(best, {c, path});
  }

  vi path = best.second;

  string dirs = "^>v<";
  string commands(KK,'?');
  rep(i,0,KK) {
    rep(d,0,4) {
      if(nxt[d][path[i]] == path[i+1]) {
        commands[i] = dirs[d];
      }
    }
    assert(commands[i] != '?');
  }

  cout << commands << endl;
}
