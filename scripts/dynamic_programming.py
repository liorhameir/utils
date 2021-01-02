from typing import List
"""
dynamic programing solutions
"""


def coin_change(coins: List[int], change: int) -> int:
    """
    the coin change problem
    :param coins: lists of coins
    :param change: the change that the we should return to the customer
    :return: minimum coins that their sum equals to the change
    """
    matrix = [[0 for m in range(change + 1)] for m in range(len(coins) + 1)]
    for i in range(change + 1):
        matrix[0][i] = i
    for c in range(1, len(coins) + 1):
        for r in range(1, change + 1):
            if coins[c - 1] == r:
                matrix[c][r] = 1
            elif coins[c - 1] > r:
                matrix[c][r] = matrix[c - 1][r]
            else:
                matrix[c][r] = min(matrix[c - 1][r], 1 + matrix[c][r - coins[c - 1]])
    for c in range(0, len(coins) + 1):
        for r in range(0, change + 1):
            print(matrix[c][r], "|", end="")
        print()
    return matrix[-1][-1]


def longest_path(numbers_list: List[int]) -> int:
    """
    given a list of numbers, find the longest increasing subsequence.
    :param numbers_list:
    :return: longest increasing subsequence
    """
    matrix = [1 for m in range(len(numbers_list))]
    for i in range(len(numbers_list)):
        for j in range(i):
            if numbers_list[i] > numbers_list[j]:
                matrix[i] = max(matrix[i], matrix[j] + 1)
    for i in matrix:
        print(i)
    return matrix[-1]


def editing_distance(str1: str, str2: str) -> int:
    """
    given two strings, return the editing distance between them
    :param str1: str
    :param str2: str
    :return: editing distance between them
    """
    if not str1 and not str2:
        return 0
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
    if str1[0] == str2[0]:
        return min(editing_distance(str1[1::], str2[1::]), 1 + editing_distance(str1, str2[1::]),
                   1 + editing_distance(str1[1::], str2))


def sequence(word1: str, word2: str) -> str:
    """
    given two strings, finds the longest mutual sequence
    :param word1: str
    :param word2: str
    :return: longest mutual sequence
    """
    matrix = [[[0, [0, 0]] for x in range(len(word1) + 1)] for i in range(len(word2) + 1)]

    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):
            # compares every letter in
            if word2[i - 1] == word1[j - 1]:
                matrix[i][j][0] = 1 + matrix[i-1][j-1][0]
                matrix[i][j][1] = [i - 1, j - 1]
            else:
                if matrix[i - 1][j][0] > matrix[i][j - 1][0]:
                    matrix[i][j][0] = matrix[i - 1][j][0]
                    matrix[i][j][1] = [i - 1, j]
                else:
                    matrix[i][j][0] = matrix[i][j - 1][0]
                    matrix[i][j][1] = [i, j - 1]
    # the code below runs in order to extract the sequence. it starts at position (m,n)
    res = ""
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    while i and j != 0:
        if matrix[i][j][1] == [i - 1, j - 1]:
            res = word1[j - 1] + res
        i, j = matrix[i][j][1]
    return res
