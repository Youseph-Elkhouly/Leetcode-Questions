class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        groups = []
        visited = set()


        for i in range(len(nums)):
            if nums[i] not in visited:
                group = [nums[j] for j in range(len(nums)) if nums[j] == nums[i]]
                groups.append(group)
                visited.add(nums[i])

        
        groups.sort(key = len, reverse = True)

        top_k_frequent = [group[0] for group in groups[:k]]    #the :k means start at the beginning of the list take up to but not including the kth element
            
        return top_k_frequent
