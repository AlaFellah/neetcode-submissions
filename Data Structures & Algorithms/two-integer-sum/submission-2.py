class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 
        # for i in range(len(nums)):
        #     s = target - nums[i]
        #     if s in nums[i+1::]:
        #         sec = nums[i+1::].index(s)
        #         ind = [i, sec+i+1]
        #         return ind
        # return []
        

        prevdiff = {}
        for i in range (len(nums)):
            if target - nums[i] in prevdiff:
                return [prevdiff[target - nums[i]], i]

            prevdiff[nums[i]] = i 

        return   

