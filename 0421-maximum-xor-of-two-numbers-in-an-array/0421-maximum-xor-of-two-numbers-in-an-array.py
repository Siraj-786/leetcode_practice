class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        trie={}


        def insert(word):
            curr=trie 
            for c in word :
                if c in curr :
                    curr=curr[c]
                else :
                    curr[c]={}
                    curr=curr[c]
            curr["*"]=True 
        max_len=max(nums).bit_length()
        for ele in nums:
            k=str(bin(ele)[2:]).rjust(max_len,"0")
            insert(k)
        max_ans=0

        def str_to_int(s1,s2):
            a=int(s1,2)
            b=int(s2,2)
            return a^b



        def for_num(k):
            num=k

            curr=trie 
            s2=[]
            for i in range(len(k)):
                if num[i]=="0" :
                    if "1" in curr :
                        s2.append("1")
                        curr=curr["1"]
                    else :
                        s2.append("0")
                        curr=curr["0"]
                else :
                    # 1 
                    if "0" in curr :
                        s2.append("0")
                        curr=curr["0"]
                    else :
                        s2.append("1")
                        curr=curr["1"]
            return str_to_int(num,"".join(s2))            


        for num in nums:
            k=str(bin(num)[2:]).rjust(max_len,"0")
            max_ans=max(max_ans,for_num(k))
        return max_ans




        