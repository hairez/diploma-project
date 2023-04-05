#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    cout.precision(20);

    int n;
    cin >> n;
    vector<int> input(n);
    for (int i = 0; i < n; ++i)
        cin >> input[i];
    vector<int> sorted = input;
    sort(begin(sorted), end(sorted));
    int ans = 0;
    for (int i = 0; i < n; ++i)
        if (input[i] != sorted[i])
            ++ans;
    cout << ans << endl;
}