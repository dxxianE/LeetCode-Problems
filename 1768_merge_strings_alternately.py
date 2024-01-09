"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters 
in alternating order, starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

"""

#first version using string:
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word = ""
        
        w1_len = len(word1)
        w2_len = len(word2)

        wt = w1_len + w2_len

        for letter in range(wt):
            if letter < w1_len:  
                word += word1[letter]
            if letter < w2_len:
                word += word2[letter] 

        print(word)
        return word

#second version using list, append and join (best runtime and memory usage)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word = []
        
        w1_len = len(word1)
        w2_len = len(word2)

        wt = w1_len + w2_len

        #This for can be changed by a while and it would be more optimal.
        for letter in range(wt):
            if letter < w1_len:  
                word.append(word1[letter])
            if letter < w2_len:
                word.append(word2[letter])

        word = ''.join(word)
        print(word)
        return word