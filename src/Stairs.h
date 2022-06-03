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
        return fibonacci[2];    //When i = n - 1, fibonacci[2] = nth fibonacci sequence number
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


#endif //LEETCODE_STAIRS_H
