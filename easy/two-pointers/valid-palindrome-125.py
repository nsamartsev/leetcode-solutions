class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        s_len = len(s)
        if not s or s_len == 1:
            return True
        answer = True
        start = 0
        end = s_len - 1
        s = s.lower()
        while start < end:
            left_symbol = s[start]
            right_symbol = s[end]

            if (left_symbol.isalpha() or left_symbol.isdigit()) and (
                    right_symbol.isalpha() or right_symbol.isdigit()) and left_symbol != right_symbol:
                answer = False
                break
            elif not left_symbol.isalpha() and not left_symbol.isdigit():
                start = start + 1
                continue
            elif not right_symbol.isalpha() and not right_symbol.isdigit():
                end = end - 1
                continue

            start = start + 1
            end = end - 1

        return answer


def main():
    assert Solution().isPalindrome("aba") == True
    assert Solution().isPalindrome("abb") == False
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True


if __name__ == "__main__":
    main()
