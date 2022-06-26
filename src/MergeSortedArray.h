//
// Created by Paul Woo on 26/06/22.
//

#ifndef LEETCODE_MERGESORTEDARRAY_H
#define LEETCODE_MERGESORTEDARRAY_H


class MergeSortedArray {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
    {
        // swift m elements in nums1 towards the right side by n positions
        for(int i=m+n-1;i>=n;i--)
        {
            nums1[i] = nums1[i-n];
        }

        int ind1 = n; // index to iterate over first sorted array -> nums1
        int ind2 = 0; // index to iterate over second sorted array -> nums2
        int ind = 0; // index to iterate over nums1 for storing resulting sorted array.

        while(ind1<m+n && ind2<n)
        {
            if(nums1[ind1]<nums2[ind2])
            {
                nums1[ind] = nums1[ind1];
                ind++; ind1++;
            }
            else
            {
                nums1[ind] = nums2[ind2];
                ind++; ind2++;
            }
        }

        // if elements left in nums2, write to the resulting array
        while(ind2<n)
        {
            nums1[ind] = nums2[ind2];
            ind++; ind2++;
        }

        // if elements left in nums1, they will be in their desired final positions only


    }
};

#endif //LEETCODE_MERGESORTEDARRAY_H
