class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        start = 0
        end = n - 1

        while start < end:
            if s[start] != s[end]:
                i = s[start + 1:end + 1]
                j = s[start:end]
                return i == i[::-1] or j == j[::-1]
            start = start + 1
            end = end - 1

        return True


def main():
    assert Solution.isPalindrome(Solution(), "abba") == True
    assert Solution.isPalindrome(Solution(), "abb") == True
    assert Solution.isPalindrome(Solution(), "madame") == True
    assert Solution.isPalindrome(Solution(), "dead") == True
    assert Solution.isPalindrome(Solution(), "abca") == True
    assert Solution.isPalindrome(Solution(), "tebbem") == False
    assert Solution.isPalindrome(Solution(), "eeccccbebaeeabebccceea") == False


if __name__ == "__main__":
    main()
