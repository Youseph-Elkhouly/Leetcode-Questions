class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        '''
        given an array named prices

        prices[i] is the price of a given stock on the i'th day 


        Goal: 
        Maximize the profit by choosing a single day to buy one stock 
        
        and choosing a different day in the future to sell that stock


        return max profit you can acheieve from this transaction 
        
        if you cant achieve any profit return 0

        
        
        
        
        
        
        PSUEDOCODE:        
            
            Initialize LEFT = 0                 // buy pointer
            Initialize RIGHT = 1                // sell pointer
            Initialize maxProfit = 0            // tracks highest profit so far

            WHILE RIGHT < length(prices):

                IF prices[RIGHT] < prices[LEFT]:
                    // found cheaper price to buy
                    LEFT = RIGHT

                ELSE:
                    // calculate current profit
                    currentProfit = prices[RIGHT] - prices[LEFT]

                    // update maxProfit if this profit is higher
                    IF currentProfit > maxProfit:
                        maxProfit = currentProfit

                // always move RIGHT one step forward
                RIGHT = RIGHT + 1

            RETURN maxProfit



        '''



        LEFT = 0 #buy pointer
        RIGHT = 1 #sell pointer 
        maxProfit = 0 #tracks the highest profit so far


        while RIGHT < len(prices):
            if prices[RIGHT] < prices[LEFT]:
                #This condition means there is a cheaper price to go in at (buy)
                LEFT = RIGHT
            else:
                #we need to calculate the current profit
                currentProfit = prices[RIGHT] - prices[LEFT]


                #next we need to update maxProfit int if the profit is higher ONLY!!
                if currentProfit > maxProfit:
                    maxProfit = currentProfit

            RIGHT = RIGHT + 1

        return maxProfit


        
