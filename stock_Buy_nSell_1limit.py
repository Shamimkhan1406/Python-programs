def maxProfit(prices):
    res = 0
    minSofar = prices[0]
    for i in range (1,len(prices)):
        minSofar = min(minSofar,prices[i])
        res = max (res, prices[i]-minSofar)
    return res
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
# Time Complexity: O(n)
# Space Complexity: O(1)