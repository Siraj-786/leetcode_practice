class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi=max(nums)
        def for_multiple_indices(ind,arr)-> int:
            ans=1
            i=ind-1
            j=ind+1 
            curr=1
            while (i>=0 or j<len(nums)):
                if i>=0 :
                    if nums[i]==arr[ind] :
                        ans+=1
                        i-=1
                        continue 
                if j<len(nums):
                    print("kk")
                    if nums[j]==arr[ind] :
                        print("kkkk")
                        ans+=1
                        j+=1 
                
                curr+=1
                if ans!=curr :
                    break 
            print("ans",ans)
            return ans
        multiple_indices=[]
        for i in range(len(nums)):
            if i==0 :
                if nums[i]==maxi :
                    multiple_indices.append(i)
            else :
                if nums[i]==maxi and nums[i]!=nums[i-1] :
                    multiple_indices.append(i)
        print(multiple_indices)
        maxi=1
        for indices in multiple_indices :
            maxi=max(maxi,for_multiple_indices(indices,nums))
        return maxi





        