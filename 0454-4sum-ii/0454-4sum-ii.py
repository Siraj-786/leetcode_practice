class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:      
        arr1=nums1
        arr2=nums2
        arr3=nums3
        arr4=nums4
        new1=[]
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                new1.append(arr1[i]+arr2[j])
        # print(new1)
        c=defaultdict(int)
        for i in range(len(arr3)):
            for j in range(len(arr4)):
                c[arr3[i]+arr4[j]]+=1
        # print(c)
        ans=0

        for ele in new1 :
            if (-1)*ele in c :
                ans+=c[(-1)*ele]
        return ans
        
        