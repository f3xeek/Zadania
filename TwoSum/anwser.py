class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsS=sorted(nums)
        lower= 0
        higher=len(numsS)-1
        summed= numsS[lower]+numsS[higher]
        while summed != target:
            if summed>target:
                higher-=1
            else:
                lower+=1
            summed= numsS[lower]+numsS[higher]
        output1=nums.index(numsS[lower])
        output2=nums.index(numsS[higher])
        if output1!=output2:
            return [output1,output2]
        return [output1,[i for i, n in enumerate(nums) if n == numsS[higher]][1]]
