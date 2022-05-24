class ThreeSum:
    def threeSum(nums):
        result = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threesum = n + nums[left] + nums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    result.append([n, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
