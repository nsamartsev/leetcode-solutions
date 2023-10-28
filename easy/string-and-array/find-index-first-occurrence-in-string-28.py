class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        first_index: int = -1

        for i in range(n):
            if haystack[i:i + len(needle)] == needle:
                first_index = i
                break

        return first_index


assert Solution().strStr("mississippi", "issip") == 4
