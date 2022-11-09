def minstock(stock_price):
    prefix = []
    price_sum = 0
    for price in stock_price:
        price_sum += price
        prefix.append(price_sum)
    min_avg = float('inf')
    for i in range(len(stock_price)-1):
        left_sum = prefix[i]
        right_sum = price_sum - left_sum
        left_avg = left_sum//(i+1)
        right_avg = right_sum//(len(stock_price)-(i+1))
        min_avg = min(min_avg, abs(left_avg - right_avg))
    return min_avg


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minstock([1,3,2,3]))
