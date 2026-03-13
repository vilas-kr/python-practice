'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without 
duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" 
and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and 
not a substring.
'''


def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            unique = set()
            for j in range(i, len(s)):
                if s[j] in unique:
                    break
                unique.add(s[j])

            max_len = len(unique) if max_len < len(unique) else max_len
        return max_len