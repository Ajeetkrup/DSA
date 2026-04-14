"""
    Finds the length of the longest substring without repeating characters.

    Approach:
    - Iterate through each character as a starting point.
    - Use a hash map (dictionary) to track character frequency.
    - Expand the substring until a duplicate character is found.
    - Update the maximum length whenever a valid substring is found.

    Example:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with length 3.

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b".

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke".

    Time Complexity:
        O(n^2) — Nested loops to explore all substrings.

    Space Complexity:
        O(k) — Hash map storing at most k unique characters
                (k = size of character set).

    Notes:
    - This is a brute-force + hashing approach.
    - Can be optimized to O(n) using sliding window technique.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        maxLen = 1

        for i in range(len(s)):
            ch_cnt = {s[i]: 1}
            substr = s[i]

            for j in range(i+1, len(s)):
                ch_cnt[s[j]] = ch_cnt.get(s[j],0)+1
                substr += s[j]

                if ch_cnt[s[j]] >= 2:
                    break

                maxLen = max(maxLen, len(substr))

        return maxLen
    
"""
    Approach 2:
    - Use two pointers (left, right) to represent a dynamic window.
    - Expand the window by moving `right`.
    - If a duplicate character is found, shrink the window from the left
        until the duplicate is removed.
    - Track the maximum length of a valid window.

    Time Complexity:
        O(n) — Each character is processed at most twice
                (once by `right`, once by `left`).

    Space Complexity:
        O(k) — Set stores at most k unique characters
                (k = size of character set).

    Sliding Window Insight:
    - `right` pointer expands the window (explores new characters).
    - `left` pointer shrinks the window (removes duplicates).
    - The window always contains unique characters.

    Key Operations:
    - `while s[right] in seen`: Detects violation (duplicate).
    - `seen.remove(s[left])`: Removes leftmost character.
    - `left += 1`: Shrinks window.
    - `seen.add(s[right])`: Adds new character to window.
    - `maxLen = max(...)`: Updates best result.

    Notes:
    - This is the optimal solution for this problem.
    - Common sliding window pattern for "longest substring with constraint".
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        maxLen = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            maxLen = max(maxLen, right-left+1)

        return maxLen