class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1>nums2:
            nums1,nums2=nums2,nums1

        n,m=len(nums1),len(nums2)
        left,right=0,n

        while left<=right:
            cut1=(left+right)//2
            cut2=(n+m+1)//2-cut1

            left1=float('-inf') if cut1==0 else nums1[cut1-1]
            right1=float('inf') if cut1==n else nums1[cut1]

            left2=float('-inf') if cut2==0 else nums2[cut2-1]
            right2=float('inf') if cut2==m else nums2[cut2] 

            if left1<=right2 and left2<=right1:
                if (n + m) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
                

            elif left1>right2:
                right=cut1-1
            else:
                left=cut1+1
        return 0.0