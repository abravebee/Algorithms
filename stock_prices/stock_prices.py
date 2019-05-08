#!/usr/bin/python

import argparse

def find_max_profit(prices):
    #if prices length == 0
    if len(prices) == 0:
        cur_max_profit = 0 #can't buy or sell to make or lose profit
    elif len(prices) == 1:
        cur_max_profit = -(prices[0]) #can only purchase, negative profit
    else:
        cur_min = prices[0]
        cur_max_profit = -(prices[0])
        print(f"START\ncur_min: {cur_min}, cur_max_profit: {cur_max_profit}")
        i = 0
        for i in range(i, len(prices)-1):
            if prices[i] <= cur_min:    
                cur_min = prices[i]
                print(f"cur_min: {cur_min}")
            if i == (len(prices)-1) and cur_min == prices[i]:
                    print(f"max in last item: {cur_max_profit}")
                    profit = -(prices[i])
                    print(f"profit in last item: {profit}")
                    if profit > cur_max_profit:
                        cur_max_profit = profit
                        return cur_max_profit
            if (prices[i+1] - cur_min) > cur_max_profit:
                cur_max_profit = (prices[i+1] - cur_min)
                print(f"cur_max_profit: {cur_max_profit}")



    return cur_max_profit

        #loop thru range(i, prices length)
            #if prices[i] < cur_min
                #cur_min = prices[i]
            #if prices[i] - cur_min >= cur_max_profit
                #cur_max_profit = (prices[i] - cur_min)
        #return cur_max_profit



    #input: list of prices
    #output: max profit from single buy/sell
    #must buy, then sell
    #subtract x from y, with y coming before x in the list
    #edge cases:
        #empty array: 0
        #single item: -n (have to buy first, so no profit, only loss of purchase price)
        #2 items: return prices[1] - prices[0]
    pass

emptyArr = []
singlePrice = [5]
expect6 = [10, 7, 5, 8, 11, 9]
expectNeg10 = [100, 90, 80, 50, 20, 10]
expect3530 = [1050, 270, 1540, 3800, 2]
expect94 = [100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]

print(find_max_profit(expect6))
print(find_max_profit(expectNeg10))
print(find_max_profit(expect3530))
print(find_max_profit(expect94))


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))