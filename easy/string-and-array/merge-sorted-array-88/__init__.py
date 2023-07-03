from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        start = m
        end = m + n - 1

        i = 0
        while start <= end:
            nums1[start] = nums2[i]
            start = start + 1
            i = i + 1

        nums1.sort()


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == "__main__":
    main()
