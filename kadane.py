#kadane's algorithm

#used in finding maximum sub array 

 def maxSubArray(self, nums: List[int]) -> int:
        max_so_far= nums[0]
        max_ending_here=0
        n=len(nums)
        start=0
        end=0
        s=0
        for i in range(0,n):
            max_ending_here+=nums[i]
            
            if(max_so_far<max_ending_here):
                max_so_far=max_ending_here
                start=s
                end=i
            if(max_ending_here<0):
                max_ending_here=0
                s=i+1
        return max_so_far
