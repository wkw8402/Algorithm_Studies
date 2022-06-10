//
// Created by Paul Woo on 03/06/22.
//

#ifndef LEETCODE_STAIRS_H
#define LEETCODE_STAIRS_H
#include <vector>
#include <map>

using std::vector;
using std::map;

class Stairs {
public:
    int climbStairs(int n) {
        vector<int> fibonacci(3, 1);
        for (int i = 1; i < n; i++) {   //When i = 1, fibonacci[2] = 2nd fibonacci sequence number
            fibonacci[2] = fibonacci[1] + fibonacci[0];
            fibonacci[0] = fibonacci[1];
            fibonacci[1] = fibonacci[2];
        }
        return fibonacci[2];    //When i = N - 1, fibonacci[2] = nth fibonacci sequence number
    }
};

map<int,int> dp;
int memoized(int n) {
    if(n<=2) return n;
    else
    {
        if(dp[n]!=0) return dp[n];
        dp[n]= memoized(n-1) + memoized(n-2);
        return dp[n];
    }
}

#include <iostream>

int countPrime(int n)
{
    int poss = 0;
    vector<int> primes; //vector to store all prime numbers in non-descending order
    for (int i = 2; i <= n; i++) {
        if (isPrime(i)) {
            primes.push_back(i);
        }
    }

    int sum = primes[0];
    for (int i = 1; i < primes.size(); i++) {
        sum += primes[i];
        if (sum > n)
            break;
        if (isPrime(sum)) { //increment poss only if the sum is also a prime number
            poss++;
        }
    }
    return poss;
}

int main(){
    int x;

    std::cin >> x;
    std::cout << countPrime(x);

    return 0;
}

bool isPrime(int n) //finding prime numbers in between 1 to N
{
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;

    for (int i = 5; i * i <= n; i = i + 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }
    return true;
}




#endif //LEETCODE_STAIRS_H
