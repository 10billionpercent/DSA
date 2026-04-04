class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = set()
        l = 0
        max_len = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len       