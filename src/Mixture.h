#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int N;
    cin >> N;

    int start = 0;
    int end = N - 1;
    int min = 2000000001;
    int arr[N];

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    while(start < end) { //using two pointer algorithm
        int sum = arr[start] + arr[end];
        if(abs(sum) < min) {
            min = abs(sum);
        }
        if(sum < 0) start++;
        else end--;
    }

    cout << min;
    return 0;
}