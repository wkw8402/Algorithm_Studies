//
// Created by Paul Woo on 26/05/22.
//

#ifndef LEETCODE_SUDOKU_H
#define LEETCODE_SUDOKU_H
#include <unordered_set>
#include <vector>
#include <iostream>

using std::unordered_set;
using std::vector;
using namespace std;

class sudoku {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        //checking rows
        unordered_set<char> row;
        for (int i = 0; i < board.size(); i++) {
            row.clear();
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == '.') continue;
                if (row.find(board[i][j]) == row.end()) {
                    row.insert(board[i][j]);
                } else {
                    return false;
                }
            }
        }

        //checking columns
        unordered_set<char> column;
        for (int i = 0; i < board[0].size(); i++) {
            column.clear();
            for (int j = 0; j < board.size(); j++) {
                if (board[i][j] == '.') continue;
                if (column.find(board[i][j]) == column.end()) {
                    column.insert(board[i][j]);
                } else {
                    return false;
                }
            }
        }

        //checking sub-boxes
        unordered_set<char> box;
        for (int i = 0; i < board.size(); i += 3) {
            for (int j = 0; j < board[0].size(); j += 3) {
                box.clear();
                for (int k = i; k < i + 3; k++) {
                    for (int l = j; l < j + 3; l++) {
                        if (board[k][l] == '.') continue;
                        if (box.find(board[k][l]) == box.end()) {
                            box.insert(board[k][l]);
                        } else {
                            return false;
                        }
                    }
                }
            }
        }

        //passed all three tests
        return true;
    }
};


#endif //LEETCODE_SUDOKU_H
