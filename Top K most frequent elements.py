"""
Approach: Max Heap (Priority Queue) using Frequency Map

Description:
- Count the frequency of each element using a hashmap (dictionary).
- Push elements into a max heap based on their frequency.
    - Since Python's heapq is a min heap, store (-count, num) to simulate a max heap.
- Pop the top k elements from the heap to get the k most frequent elements.

Time Complexity:
- O(n) for building the frequency map.
- O(n log n) for pushing all elements into the heap.
- O(k log n) for extracting top k elements.
- Overall: O(n log n)

Space Complexity:
- O(n) for hashmap and heap.

Pros:
- Easy to understand and implement.
- Directly gives elements in decreasing order of frequency.

Cons:
- Not optimal for large n when k is small (can be improved to O(n log k) using a min heap).
"""

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        max_heap = []
        ans = []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for num, cnt in count.items():
            heapq.heappush(max_heap, (-cnt, num))

        while max_heap:
            cnt, num = heapq.heappop(max_heap)
            ans.append(num)
            k -= 1

            if k == 0:
                break
                
        return ans