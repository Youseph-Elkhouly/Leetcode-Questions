class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        

        
        groupofAnagrams = {}

        # loop through the string in the input list
        for s in strs:

            #sorting the character in the string 
            sorted_string = ''.join(sorted(s))

            # if it doesnt exist create a new list 
            if sorted_string not in groupofAnagrams:
                groupofAnagrams[sorted_string] = []

            #add the original string to the list
            groupofAnagrams[sorted_string].append(s)

        #then return all the grouped anagrams as a list of list since it specifies rtype: List[List[str]]
        return list(groupofAnagrams.values())

