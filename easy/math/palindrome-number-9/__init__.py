class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            xstr = str(x)
            xstr_len = len(xstr)

            for i in range(xstr_len):
                if xstr[i] != xstr[xstr_len - 1 - i]:
                    return False

            return True
        return False


def main():
    assert Solution.isPalindrome(Solution(), 131) == True
    assert Solution.isPalindrome(Solution(), 122) == False


if __name__ == "__main__":
    main()
