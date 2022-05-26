cmake_minimum_required(VERSION 3.22)
project(LeetCode)

set(CMAKE_CXX_STANDARD 14)

include_directories(src)

add_executable(sudoku src/Sudoku.cpp)