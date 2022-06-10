#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N;
int possibility = 0;
vector<int> primes;
vector<bool> isPrime;

int main(void){
    cin >> N;
    isPrime.resize(N + 1, true);

    for (int i = 2; i <= sqrt(N); i++){
        if (!isPrime[i]) continue;
        for (int j = i * i; j <= N; j += i){
            isPrime[j] = false;
        }
    }
    for (int i=2; i <= N; i++) {
        if (isPrime[i]) primes.push_back(i);
    }

    int front = 0;
    int next = 0;
    int sum = 2;

    while(front <= next && next < (int) primes.size()){
        if(sum == N) {
            possibility++;
            sum -= primes[front];
            front++;
        }
        else if(sum < N){
            next++;
            sum += primes[next];
        }
        else if(sum > N){
            sum -= primes[front];
            front++;
        }
    }
    cout << possibility << endl;

    return 0;
}