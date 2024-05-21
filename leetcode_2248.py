"""
2248. Intersection of Multiple Arrays
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].


"""

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # importing the collections module
        import collections
        # intializing the arr
        arr = []
        for num in nums:
            arr.extend(num)
        # getting the elements frequencies using Counter class
        elements_count = collections.Counter(arr)
        # printing the element and the frequency
        result = []
        for key, value in elements_count.items():
            if value == len(nums):
                result.append(key)
        return sorted(result)
        