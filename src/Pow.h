//
// Created by Paul Woo on 12/06/22.
//

#ifndef LEETCODE_POW_H
#define LEETCODE_POW_H


class Pow {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        double ans = 1;
        if (n > 0) {
            if (n % 2 == 0) ans = myPow(x * x, n / 2);
            else {
                ans = myPow(x * x, n / 2);
                ans = ans * x;
            }
        } else {
            if (n % 2 == 0) ans = myPow((1 / x) * (1 / x), n / 2 * (-1));
            else {
                ans = myPow((1 / x) * (1 / x), n / 2 * (-1));
                ans = ans * (1 / x);
            }
        }
        return ans;
    }
};


#endif //LEETCODE_POW_H
