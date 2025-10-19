class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        '''

        #area is lxw 
        #height = area/width

        flow of program goes like this
        current heigh = z
        height of next bar = y

        if z > y then check for the max area that z couldve gotten us 
        & set the current area equals to that, and then pop z

        however when pushing onto the stack the index and the height we need
        to ensure that the z's index can be pushed backwards


        whenever popping we need to find the area that z couldve made

        '''


        maxArea = 0

        stack = []   #pair: (index, height)


        for i, h in enumerate(heights):
            #starting index is height i since we dont know if we can extend back or. no
            start = i 
#checking if not emptyy and if the top value in the stack and top val height is > currentheight reached then we need to pop height and check max rec and extend current height backwards
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index 
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
