class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n==0 or m ==0:
            if n ==0 and m==0:
                return 0
            if n == 0:
                return median(nums2)
            return median(nums1)
        for index,number in enumerate(nums1):
            while len(nums2)>0 and number>nums2[0]:
                nums1.insert(index,nums2[0])
                del nums2[0]
        if len(nums2)>0:
            nums1+=nums2
        return median(nums1)
