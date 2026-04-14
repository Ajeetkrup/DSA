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
    
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Approach:
        - Iterate through each character as a starting point.
        - Use a hash map (dictionary) to track character frequency.
        - Expand the substring until a duplicate character is found.
        - Update the maximum length whenever a valid substring is found.

        Args:
            s (str): Input string.

        Returns:
            int: Length of the longest substring without repeating characters.

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
        if len(s) == 0:
            return 0

        maxLen = 1

        for i in range(len(s)):
            ch_cnt = {s[i]: 1}
            substr = s[i]

            for j in range(i + 1, len(s)):
                ch_cnt[s[j]] = ch_cnt.get(s[j], 0) + 1
                substr += s[j]

                if ch_cnt[s[j]] >= 2:
                    break

                maxLen = max(maxLen, len(substr))

        return maxLen