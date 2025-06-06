def maxProfit(prices):
    res = 0
    for i in range (1, len(prices)):
        if(prices[i]>prices[i-1]):
            res += prices[i]-prices[i-1]
    return res
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
# Time Complexity: O(n)
# Space Complexity: O(1)