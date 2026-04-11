        """
🔤 Valid Anagram — Two HashMap Approaches

## Problem:

Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
otherwise return False.

---

## Approach 1: Basic Frequency Count

1. Check if lengths are equal.
2. Count frequency of characters in string `s`.
3. Traverse string `t` and decrement counts (if character exists).
4. Finally, check if any character count is still greater than 0.

   * If yes → not an anagram.
   * Else → valid anagram.

⚠️ Limitation:

* Does not explicitly handle:
  • Characters in `t` not present in `s`
  • Negative counts

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        word_count = {}

        for ch in s:
            if ch in word_count:
                word_count[ch] += 1
            else:
                word_count[ch] = 1

        for ch in t:
            if ch in word_count:
                word_count[ch] -= 1

        for ch in word_count:
            if word_count[ch] > 0:
                return False;

        return True

"""

Approach 2: Optimized & Safe Frequency Map

1. Check if lengths are equal.
2. Count frequency of characters in string `s` using `.get()`.
3. Traverse string `t`:

   * If character not in dictionary OR count is zero → return False.
   * Else decrement count.
4. If all checks pass → strings are anagrams.

✅ Advantages:

* Handles missing characters
* Prevents negative counts
* Early exit improves performance

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        word_count = {}

        for ch in s:
            word_count[ch] = word_count.get(ch, 0) + 1

        for ch in t:
            if ch not in word_count or word_count[ch] == 0:
                return False
                
            word_count[ch] -= 1

        return True
