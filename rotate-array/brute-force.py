class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for _ in range(k):
            last = nums.pop()     # O(1) for pop last
            nums.insert(0, last)  # O(n)
