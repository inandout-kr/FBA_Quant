
class Solution:
    def maxProfit(self, prices):
        buy_price = prices[0]
        profit = 0

        for i in prices:
            if i < buy_price:
                buy_price = i

            elif i > buy_price:
                if (i - buy_price) > profit:
                    profit = i - buy_price
        return profit

a = Solution()
b = Solution()
print(a.maxProfit([7,2,5,3,6,4]))
print(b.maxProfit([27,32,15,53,26,44]))