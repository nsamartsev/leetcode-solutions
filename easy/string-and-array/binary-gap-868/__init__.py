class Solution:
    def binaryGap(self, n: int):
        n_str = format(n, 'b')
        n_str_len = len(n_str)
        max_gap_count = 0

        index_one = n_str.index('1')
        
        for i in range(1, n_str_len):
            if n_str[i] == '1':
                max_gap_count = max(max_gap_count, i - index_one)
                index_one = i

        return max_gap_count


print(Solution().binaryGap(22))
print(Solution().binaryGap(8))
print(Solution().binaryGap(6))