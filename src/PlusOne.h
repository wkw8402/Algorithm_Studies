//
// Created by Paul Woo on 20/06/22.
//

#ifndef LEETCODE_PLUSONE_H
#define LEETCODE_PLUSONE_H

class PlusOne {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size() -1;
        for(int i=n; i>=0; i--){
            if(digits[i] != 9){ //when the last digit is 1-8 then just add 1 and return
                digits[i] += 1;
                return digits;
            }
            else
                digits[i] = 0; //when the last is 9 then replace it with 0
            //now if the 2nd last number is 0-8 then it will go in the for loop and add +1 to 2nd last number and return
        }
        //else if all the numbers are 9 then all must have been replaced by 0 till now, so just add 1 at beginning. for eg: 999
        digits.insert(digits.begin(),1);
        return digits;
    }
};


#endif //LEETCODE_PLUSONE_H
