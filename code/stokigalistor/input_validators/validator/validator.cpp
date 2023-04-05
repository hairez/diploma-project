#include "validator.h"
#include <cstring>
#include <vector>

typedef long long ll;

void run() {
    int rev = Arg("reversed", 0);
    int n = Int(1, Arg("maxn", 1e6));
    Line();
    vector<int> v = SpacedInts<int>(n, 0, 1e9);
    if (rev) {
        vector<int> copy = v;
        sort(begin(copy), end(copy), greater{});
        if (v != copy)
            die("incorrect input");
    }
}