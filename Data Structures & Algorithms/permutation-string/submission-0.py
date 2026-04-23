class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1=Counter(s1)
        count_s2=Counter()
        w_size=len(s1)

        if w_size>len(s2):
            return False

        left=0
        for right in range (len(s2)):
            count_s2[s2[right]]+=1

            if (right-left)+1 > w_size:
                count_s2[s2[left]]-=1
                if count_s2[s2[left]]==0:
                    del count_s2[s2[left]]
                left+=1
            if count_s1==count_s2:
                return True
        return False


    
                