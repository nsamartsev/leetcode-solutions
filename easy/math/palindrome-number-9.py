class Solution:
    def isPalindrome(x: int) -> bool:
        if x >= 0:
            xstr = str(x)
            xstr_len = len(xstr)

            for i in range(xstr_len):
                if xstr[i] != xstr[xstr_len - 1 - i]:
                    return False

            return True
        return False


assert Solution.isPalindrome(131) == True
assert Solution.isPalindrome(122) == False
