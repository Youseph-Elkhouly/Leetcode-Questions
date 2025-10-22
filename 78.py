class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        '''
        Points: 
        1)integer array named nums 
        2)nums array is of unique elements 
        3)it returns all the possible subsets (the power set)
        4)the solution set must not contain duplicate subsets
        5)return the solution in any order
        '''


        res = []

        subset = []

        #i tells us which element weare currently visiting
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            #decision to include nums[i]

            subset.append(nums[i])
            dfs(i + 1)

            #decision to not include nums[i]

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
            
