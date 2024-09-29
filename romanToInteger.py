class Solution(object):
    def romanToInt(self, s):
        
        
        # Initialize variables
        finalNum = 0
        length = len(s)

        # Loop through the string
        for i in range(length):
            # Assign integer values based on the Roman numeral character
            if s[i] == 'I':
                value = 1
            elif s[i] == 'V':
                value = 5
            elif s[i] == 'X':
                value = 10
            elif s[i] == 'L':
                value = 50
            elif s[i] == 'C':
                value = 100
            elif s[i] == 'D':
                value = 500
            elif s[i] == 'M':
                value = 1000

            # Check if this character needs to be subtracted or added
            if i < length - 1:
                # If current value is less than the next, subtract it
                if ((s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X')) or
                    (s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C')) or
                    (s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'))):
                    finalNum -= value
                else:
                    finalNum += value
            else:
                finalNum += value  # Add value for the last character

        return finalNum


'''
13. Roman to Integer
Solved
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

'''
