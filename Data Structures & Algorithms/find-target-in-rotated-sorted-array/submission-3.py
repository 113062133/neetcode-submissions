class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = -1

        while left < right:
            if nums[left] < nums[right]:
                break
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        
        if pivot == 0:
            left = 0
            right = len(nums) - 1
        elif target >= nums[0]:
            left = 0
            right = pivot - 1
        else:
            left = pivot
            right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1