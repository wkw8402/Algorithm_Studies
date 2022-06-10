#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(0);

    int N;
    int times;
    int index;
    int cumulative = 0;
    int minTime = 0;

    cin >> N;
    vector<int>time(N, 0);

    for (index = 0; index < N; ++index) {
        cin >> times;
        time.push_back(times);
    }

    sort(time.begin(), time.end());

    time.pop_back();

    for(int i=0; i<N; i++){
        minTime += (N-i)*time[i];
    }

    cout << minTime;
    return 0;
}