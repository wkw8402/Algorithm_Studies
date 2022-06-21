//
// Created by Paul Woo on 21/06/22.
//

#ifndef LEETCODE_SQRTX_H
#define LEETCODE_SQRTX_H


class SqrtX {
public:
    int mySqrt(int x) {
        return binarySearch(x);
    }

    long long int binarySearch(int n){
        int start = 0; //Draw a number line from 0 to x.
        int end = n;
        long long int mid = start+(end-start)/2; //Now we know that square root lies between 0 to x.
        long long int ans = -1;

        while(start<=end){          //Now apply binary search and find the solution in O(log N).
            long long int square = mid*mid;

            if(square == n){
                return mid;
            }

            if(square < n){
                ans=mid;
                start=mid+1;
            }else {
                end=mid-1;
            }
            mid = start+(end-start)/2;
        }
        return ans;
    }
};


#endif //LEETCODE_SQRTX_H
