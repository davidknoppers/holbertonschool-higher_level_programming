#!/usr/bin/python3
"""
References:
Google https://developers.google.com/optimization/puzzles/queens#python
Geeks for Geeks
http://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/
Tushar Roy https://youtu.be/xouin83ebxE
Rosetta Code https://rosettacode.org/wiki/N-queens_problem#Python
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    N = int(sys.argv[1])
except:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def under_attack(col, queens):
    if col in queens:
        return True
    elif any(abs(col - x) == len(queens) - i for i, x in enumerate(queens)):
        return True
    return False


def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = [solution+[i+1]
                     for solution in solutions
                     for i in range(N)
                     if not under_attack(i+1, solution)]
    return solutions
result = []
solutions = solve(N)
for solution in solutions:
    temp = []
    for i in range(len(solution)):
        temp.append([i, solution[i] - 1])
    result.append(temp)
for r in result:
    print(r)
