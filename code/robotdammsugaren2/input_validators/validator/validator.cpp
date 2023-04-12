#include "validator.h"

void run() {
	int T = Int(0, 10);
	assert(T == (int)Arg("t"));
	Endl();
	int R = Int(1, 2000);
	Space();
	int C = Int(1, 2000);
	Space();
	int N = Int(1, 2000);
	Endl();
	int starts = 0;
	for(int i = 0; i < R; i++){
		string s = Line();
		assert(s.length() == C);
		assert(s[0] == '#');
		assert(s[C-1] == '#');
		for(int j = 0; j < C; j++){
			if(i == 0 || i == R-1){
				assert(s[j] == '#');
			}
			else{
				assert(s[j] == '#' || s[j] == '.' || s[j] == 'O');
			}
			if(s[j] == 'O')starts++;
		}
	}
	assert(starts == 1);
}
