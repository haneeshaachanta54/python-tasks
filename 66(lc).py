class Solution(object):
    def plusOne(self, digits):
        num = ""
        for d in digits:
            num += str(d)
        num = int(num) + 1
        result = []
        for ch in str(num):
            result.append(int(ch))
        return result