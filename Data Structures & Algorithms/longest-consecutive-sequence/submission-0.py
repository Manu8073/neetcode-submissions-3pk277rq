class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

      num_set=set(nums)
      longest=0

      for i in nums:
        if i-1 not in num_set:
          current=i
          lenght=1

          while current+1 in num_set:
            current+=1
            lenght+=1
          longest=max(longest,lenght)
      return longest


        