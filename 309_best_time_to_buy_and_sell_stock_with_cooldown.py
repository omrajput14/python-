# 309. Best Time to Buy and Sell Stock with Cooldown
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

def max_profit(prices):
    sold, held, reset = float('-inf'), float('-inf'), 0
    for price in prices:
        pre_sold = sold
        sold = held + price
        held = max(held, reset - price)
        reset = max(reset, pre_sold)
    return max(sold, reset)

if __name__ == "__main__":
    print(max_profit([1,2,3,0,2]))
