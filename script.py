def maxProfit(k, prices):
    n = len(prices)
    if n <= 1:
        return 0
    if k >= n // 2:
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
 
    dp = [[0] * n for _ in range(k + 1)]
    
    for trans in range(1, k + 1):
        max_diff = -prices[0]
        for day in range(1, n):
            dp[trans][day] = max(dp[trans][day - 1], max_diff + prices[day])
            max_diff = max(max_diff, dp[trans - 1][day] - prices[day])
    
    return dp[k][-1]

#test de challenge
k1 = 2
prices1 = [2, 4, 1]
print(maxProfit(k1, prices1))

#test de challenge
k2 = 2
prices2 = [3, 2, 6, 5, 0, 3]
print(maxProfit(k2, prices2))

k = int(input("Entrez la valeur de k : "))
prices = list(map(int, input("Entrez les prix separes par des espaces expl : 2 4 1 >>").split()))
print("Le profit maximal est :", maxProfit(k, prices))