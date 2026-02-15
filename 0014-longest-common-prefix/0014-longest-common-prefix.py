class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """ 
        common = "" 
        for i in range(len(strs[0])):
                if all(len(word) > i and word[i] == strs[0][i] for word in strs):
                    common += strs[0][i]
                else:
                    break
        return common
        