def maxProfit(prices):
    n=len(prices)
    if n<2:
        return 0
    left=[0]*n
    right=[0]*n

    minPrice = prices[0]
    for i in range(1, n):
        left[i] = max(left[i-1],prices[i]-minPrice)
        minPrice = min(minPrice,prices[i])

    maxPrice = prices[n-1]
    for i in range(n-2,-1,-1):
        right [i] = max(right [i+1],maxPrice-prices[i])
        maxPrice = max(maxPrice, prices[i])

    maxProfit=0
    for i in range(n):
        maxProfit=max(maxProfit,left[i]+right[i])

    return maxProfit

prices =[7,6,4,3,1] 
print ("Maximum profit: ", maxProfit(prices))
 
