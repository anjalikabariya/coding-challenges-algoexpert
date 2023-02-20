''' <div class="html">
  Given an array of positive integers representing the values of coins in your
  possession, write a function that returns the minimum amount of change (the
  minimum sum of money) that you <b>cannot</b> create. The given coins can have
  any positive integer value and aren't necessarily unique (i.e., you can have
  multiple coins of the same value).
  For example, if you're given coins = [1, 2, 5], the minimum
  amount of change that you can't create is 4. If you're given no
  coins, the minimum amount of change that you can't create is 1.

Sample Input
coins = [5, 7, 1, 1, 2, 3, 22]

Sample Output
20'''

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    if not coins or coins[0] != 1:
        return 1
    # coin[0] = 1
    ans = 2
    for i in range(1, len(coins)):
        if coins[i] > ans:
            return ans
        ans = ans + coins[i]
    return ans
    
