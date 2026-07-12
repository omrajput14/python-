def max_profit(prices):
    if not prices: return 0
    min_price = prices[0]
    max_prof = 0
    for price in prices:
        if price < min_price: min_price = price
        elif price - min_price > max_prof: max_prof = price - min_price
    return max_prof

if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))