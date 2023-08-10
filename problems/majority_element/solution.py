class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        n_by_2 = len(nums)//2
        major_ele = None
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else: 
                count_dict[num] += 1

        for k,v in count_dict.items():
            if count_dict[k] > n_by_2:
                return k
            
