# https://leetcode.com/problems/richest-customer-wealth
# Richest Customer Wealth

accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

def maxwealth():
    sums = []
    for i in accounts:
        sums.append(sum(i))
    return max(sums)

print(maxwealth())


