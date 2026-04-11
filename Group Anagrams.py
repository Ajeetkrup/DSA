"""
🔤 Group Anagrams — Brute Force vs Optimized Approach (Python)

Problem:

Given a list of strings strs, group the anagrams together.
Return the result as a list of groups.

Approach 1: Brute Force using isAnagram
1.Iterate through each string.
2.For every string, compare it with the remaining strings using isAnagram.
3.If two strings are anagrams → group them together.
4.Use a dictionary (isProcessed) to avoid re-processing elements.

⚠️ Drawbacks:

* Repeated comparisons (redundant work)
* Not scalable for large inputs

Time Complexity: O(n² * k)
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        isProcessed = {}

        for i in range(len(strs)):
            if i not in isProcessed:
                group = [strs[i]]
                isProcessed[i] = True

                for j in range(i+1,len(strs)):
                    if j not in isProcessed and self.isAnagram(strs[i], strs[j]):
                        group.append(strs[j])
                        isProcessed[j] = True
                result.append(group)

        return result

"""
Approach 2: Optimized using Frequency Count (Hashing)

1. For each word, create a frequency array of size 26.
2. Use `ord(c) - ord('a')` to map characters to indices.
3. Convert frequency list to tuple → use as dictionary key.
4. Group words with the same frequency signature.

✅ Advantages:

* No pairwise comparison
* Efficient grouping using hashing
* Best approach for interviews

Time Complexity: O(n * k)
Space Complexity: O(n * k)

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            ch = [0]*26

            for c in word:
                ch[ord(c) - ord("a")] += 1

            ans[tuple(ch)].append(word)

        return list(ans.values())