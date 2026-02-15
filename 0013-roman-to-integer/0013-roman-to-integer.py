class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        num = 0
        traversed = ""
        for i in s:
            if traversed != "":
                if roman[i] > roman[traversed[-1]]:
                   num += roman[i] - 2*roman[traversed[-1]]
                   continue
            num += roman[i]
            traversed += i
        return num
        