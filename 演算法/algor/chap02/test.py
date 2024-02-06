class Solution:

    def rob(self, nums) :
        if len(nums) ==0:
            return nums[0]
        else :
            for i in range(1,len(nums)):
                if i ==1:
                    if nums [0]>nums[1]:
                        nums[1]=nums[0]
                    else :
                        pass
                else :
                    k=nums[i-1]
                    l=nums[i-2]+nums[i]
                    if k>l:
                        nums[i]=k
                    else :
                        nums[i]=l
            return nums[len(nums)-1]
a= Solution()

b=[1,2,3,1]
print(a.rob(b))