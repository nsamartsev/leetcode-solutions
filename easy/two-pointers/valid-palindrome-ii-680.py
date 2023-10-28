class Solution(object):
    def isPalindrome(self: str) -> bool:
        n = len(self)
        start = 0
        end = n - 1

        while start < end:
            if self[start] != self[end]:
                s1 = self[start + 1:end + 1]
                s2 = self[start:end]
                return s1 == s1[::-1] or s2 == s2[::-1]
            start = start + 1
            end = end - 1

        return True


assert Solution.isPalindrome("abba")
assert Solution.isPalindrome("abb")
assert Solution.isPalindrome("madame")
assert Solution.isPalindrome("dead")
assert Solution.isPalindrome("abca")
assert not Solution.isPalindrome("tebbem")
assert not Solution.isPalindrome("eeccccbebaeeabebccceea")
