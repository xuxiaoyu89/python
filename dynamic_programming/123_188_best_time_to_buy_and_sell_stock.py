'''
123.
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
'''
'''

buy1	-> keep it as low as possible 	-> max(buy1, -i)
sell1	-> keep it as high as possible	-> max(sell1, buy1 + i)
buy2	-> keep it as low as possible	-> max(buy2, sell1 - i)
sell2	-> keep it as high as possible  -> max(sell2, buy2 + i)

state machine

for every price, calculate max for each state

'''

'''
188.
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
'''

'''
price: 
a b c d e f g h i j k

dp[i, j] = max(dp[i-1][j], dp[i-1][k] + stock[j] - stock(k))
	     = max(dp[i-1][j], stock[j] + max(dp[i-1][k] - stock(k)) ( 0 <= k < j)    )


	     partial[k] = max(dp[i-1][k] - stock(k))) where   0 <= k < j
	     			= max(partial[k-1], dp[i-1][k] - stock[k])

	     for j in range(0, n), partial can be get by previous partial.

'''