# Given two strings wild and pattern. Determine if the given two strings can be matched given that, wild string may contain * and ? but string pattern will not. * and ? can be converted to another character according to the following rules:

# * --> This character in string wild can be replaced by any sequence of characters, it can also be replaced by an empty string.
# ? --> This character in string wild can be replaced by any one character.
# Example 1:

# Input: 
# wild = ge*ks
# pattern = geeks
# Output: Yes
# Explanation: Replace the '*' in wild string 
# with 'e' to obtain pattern "geeks".

class Solution:
    def match(self, wild, pattern):
                n = len(wild)
                m = len(pattern)
                
                i, j = 0, 0
                checkpoint_wild = -1
                checkpoint_pattern = -1
                
                while j < m:
                    if i < n and (wild[i] == pattern[j] or wild[i] == '?'):
                        i += 1
                        j += 1
                    elif i < n and wild[i] == '*':
                        checkpoint_wild = i
                        checkpoint_pattern = j
                        i += 1
                    elif checkpoint_wild != -1:
                        # Backtrack to the last '*' checkpoint
                        i = checkpoint_wild + 1
                        j = checkpoint_pattern + 1
                        checkpoint_pattern += 1
                    else:
                        return False
                
                while i < n and wild[i] == '*':
                    i += 1
                
                return i == n and j == m

