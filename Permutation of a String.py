"""
    Approach 1: Brute Force (Sorting-Based Comparison)

    Problem:
        Check if any permutation of s1 exists as a substring in s2.

    Idea:
        - Generate all possible substrings of s2
        - Sort each substring and compare with sorted s1
        - If any match found, return True

    Time Complexity:
        O(n^2 * k log k), where k is substring length

    Space Complexity:
        O(k) for substring storage

    Note:
        This approach is not efficient for large inputs and will lead to TLE.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = "".join(sorted(s1))

        for i in range(len(s2)):
            substr = ""
            for j in range(i, len(s2)):
                substr += s2[j]

                if  "".join(sorted(substr)) == s1_sorted:
                    return True

        return False
    
"""
    Approach 2: Sliding Window + Frequency Counter (Optimal)

    Problem:
        Check if any permutation of s1 exists as a substring in s2.

    Idea:
        - Use a fixed-size sliding window of length len(s1)
        - Maintain character frequency using Counter
        - Slide window across s2 and update counts efficiently
        - Compare frequency maps instead of sorting

    Time Complexity:
        O(n), where n = len(s2)

    Space Complexity:
        O(1) (bounded alphabet size, e.g., 26 lowercase letters)

    Why better:
        Avoids sorting and reduces repeated computation using incremental updates.
"""
    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)

        s1_count = Counter(s1)
        word_count = Counter(s2[:l1])

        if s1_count == word_count:
            return True

        for i in range(l1, l2):
            word_count[s2[i]] += 1
            word_count[s2[i-l1]] -= 1

            if word_count[s2[i-l1]] == 0:
                del word_count[s2[i-l1]]

            if s1_count == word_count:
                return True

        return False