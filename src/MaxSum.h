//
// Created by Paul Woo on 27/06/22.
//

#ifndef LEETCODE_MAXSUM_H
#define LEETCODE_MAXSUM_H


class MaxSum {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int maximum = INT_MIN;

//         for(int i=0; i<nums.size();i++)
//         {
//             sum += nums[i];

//             if(maximum<sum)
//                 maximum = sum;

//             if(sum<0)
//                 sum=0;
//         }

        // Using iterator for traversal ( iterator is always faster )
        for(auto i : nums)
        {
            sum += i;

            maximum = max(maximum,sum);

            if(sum<0)
                sum = 0;
        }

        return maximum;
    }
};

#endif //LEETCODE_MAXSUM_H
