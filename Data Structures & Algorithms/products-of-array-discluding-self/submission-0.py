class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left , right = 1, 1
        left_lst = []
        right_lst = []
        for num in nums:
            left_lst.append(left)
            left *= num
        for num in nums[::-1]:
            right_lst.append(right)
            right *= num
        right_lst.reverse()
        ans = []
        for i in range(len(nums)):
            ans.append(left_lst[i] * right_lst[i])
        return ans
            
        