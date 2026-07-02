import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        A, B = (nums1, nums2) if m <= n else (nums2, nums1)
        half = (m + n) // 2

        left = 0
        right = len(A)
        while left <= right:
            mid = (left + right) // 2
            Aleft = A[mid - 1] if mid > 0 else -math.inf
            Aright = A[mid] if mid < len(A) else math.inf
            Bleft = B[half - mid - 1] if half - mid > 0 else -math.inf
            Bright = B[half - mid] if half - mid < len(B) else math.inf

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = mid - 1
            else:
                left = mid + 1