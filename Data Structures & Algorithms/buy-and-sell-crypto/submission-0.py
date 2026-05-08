class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = prices[0]
        maxprofit = 0 
        
        ind = 1 
        end = len(prices)

        while ind < end: 
            if prices[ind] < minsofar: 
                minsofar = prices[ind]
            elif prices[ind] - minsofar > maxprofit: 
                maxprofit = prices[ind] - minsofar
        
            ind += 1 
        return maxprofit