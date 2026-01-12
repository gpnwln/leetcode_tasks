class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pol = []
        for i in range(0, len(s)):
            pol.append(s[i])
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    substr = s[i:j+1]
                    if substr == substr[::-1]:
                        pol.append(substr)
        return max(pol, key=len)