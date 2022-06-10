#include <iostream>
#include <math.h>

using namespace std;

int GCD(int a, int b) {
    if (b == 0)
        return a;
    else {
        return GCD(b, a % b);
    }
}

int main() {
    int n, d, temp, mod, result = 0;
    cin >> n >> d;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        mod = abs(temp - d);
        result = GCD(mod, result);
    }
    cout << result;
    return 0;
}