class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        max_seq_length = 0
        if not nums:
            return 0

        for num in nums:
            num_set.add(num)
        for num in num_set:
            temp_seq_length = 0
            if num+1 in num_set:
                continue
            num_in_seq_lt = num-1
            while num_in_seq_lt in num_set:
                temp_seq_length += 1
                num_in_seq_lt -= 1

            if temp_seq_length > max_seq_length:
                max_seq_length = temp_seq_length

            num_set.add(num)

        return max_seq_length+1


