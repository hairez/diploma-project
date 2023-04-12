// usage: ./a.out input_file correct_output output_dir < contestants_output
#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < int(to); ++i)
#define sz(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()
#define trav(a, x) for(auto& a : x)
typedef vector<int> vi;
typedef long long ll;
typedef pair<int, int> pii;

static string input_file, output_dir, answer_file;

void die(const string& msg) {
    cout << msg << endl;
    ofstream(output_dir + "/score.txt") << 0;
    exit(43);
}

void accept(long double score) {
    ofstream(output_dir + "/score.txt") << setprecision(2) << fixed << score;
    exit(42);
}

void judge_error(const string& msg) {
	cout << msg << endl;
	exit(1);
}

template <class F>
void assert_done(istream& is, F fail) {
    try {
        string dummy;
        is >> dummy;
		if (is) fail("extraneous data: " + dummy);
    } catch(...) {}
}

pair<ll,ll> getDir(char c){
    switch(c){
        case 'v': return {1,0}; break;
        case '<': return {0,-1}; break;
        case '>': return {0,1}; break;
        case '^': return {-1,0}; break;
    }
}

template <class F>
long double score(istream& is, vector<string>& grid, int N, F fail) {
	int R = sz(grid);
	int C = sz(grid[0]);
	string answer;
	if(!(is >> answer)){
		fail("Could not read answer.\n");
	}
	assert_done(is, fail);
	if(sz(answer) != N){
		fail("Answer had invalid length.\n");
	}
	rep(c1,0,N){
		if(answer[c1] != '<' && answer[c1] != '>' && answer[c1] != '^' && answer[c1] != 'v'){
			fail("Invalid character.\n");
		}
	}
	
	// Based on 'fredrik_100.cpp'
	ll ri = -1;
    ll ci = -1;
	vector<string> grid2 = grid;
	rep(i,0,R) {
        rep(j,0,C)
            if(grid[i][j]=='O') {
                ri = i;
                ci = j;
            }
    }
	trav(c,answer){
        ll dr,dc;
        tie(dr,dc) = getDir(c);
        while(grid[ri+dr][ci+dc]!='#'){
            ri += dr; ci += dc;
            grid2[ri][ci] = ' ';
        }
    }
    ll ans = 0;
    rep(i,0,R) rep(j,0,C) ans += (grid2[i][j]==' ' || grid2[i][j]=='O');

	return ans;
}

int main(int argc, char** argv) {
    if (argc < 4) exit(1);
    cin.sync_with_stdio(0);
    cin.tie(0);

    input_file = argv[1];
    answer_file = argv[2];
    output_dir = argv[3];

    ifstream fin(input_file);
    fin.exceptions(cin.failbit | cin.badbit | cin.eofbit);

    int T;
    fin >> T;

    int R, C, N;
    fin >> R >> C >> N;

	vector<string> grid;

	rep(i,0,R){
		string line;
		fin >> line;
		grid.push_back(line);
	}

    assert_done(fin, die);
    fin.close();

	ifstream fans(answer_file);

    try {
		long double sc = score(cin, grid, N, die);
		long double bestsc = score(fans, grid, N, judge_error);
		long double ratio = sc / bestsc;
		if (T == 0) accept(0);
		else accept(10.0 * min(1.0L,ratio));
    } catch(...) {
        die("IO failure");
    }
}
