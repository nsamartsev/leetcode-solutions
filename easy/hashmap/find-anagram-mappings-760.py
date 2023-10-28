# https://leetcode.com/problems/find-anagram-mappings/

class Solution:
    @staticmethod
    def find_mapping(self, nums1, nums2):
        index_map = dict()

        for i, num in enumerate(nums2):
            index_map[num] = i

        result = [index_map[num] for num in nums1]
        return result


class Solution2:
    def find_mapping(self, nums1, nums2):
        result = {num: i for i, num in enumerate(nums2)}
        return [result[num] for num in nums1]


solution = Solution2()
assert solution.find_mapping([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]) == [1, 4, 3, 2, 0]
