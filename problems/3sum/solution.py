class Solution:
     def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(0, len(nums)):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    temp_result = sorted([nums[i], nums[j], nums[k]])
                    if temp_result not in result:
                        result.append(temp_result)
                    j = j+1

                elif nums[j] + nums[k] > -nums[i]:
                    k = k-1
                else:
                    j = j+1
            '''
            sum_i = nums[i]
            for j in range(i+1, len(nums)):
                sum_i = sum_i + nums[j]
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp_result = sorted([nums[i], nums[j], nums[k]])
                        if(temp_result not in result):
                             result.append(temp_result)
                    if sum_i + nums[k] == 0:
                        temp_result = sorted([nums[i], nums[j], nums[k]])
                        if(temp_result not in result):
                             result.append(temp_result)
                sum_i = nums[i]
            '''
        return result