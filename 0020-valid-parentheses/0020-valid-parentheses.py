class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            '[' : ']',
            '{' : '}',
            '(' : ')'
        }
        stack = []
        if len(s) == 1:
            return False
        for i in s:
            if i in brackets.keys(): #open bracket
                stack.append(i)
            else: #closed bracket
                if stack and brackets[stack[-1]] == i: #match
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
           return True
        else:
            return False