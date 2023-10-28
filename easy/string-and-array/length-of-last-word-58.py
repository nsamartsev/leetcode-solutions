class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[len(arr) - 1])


def main():
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))


if __name__ == '__main__':
    main()
