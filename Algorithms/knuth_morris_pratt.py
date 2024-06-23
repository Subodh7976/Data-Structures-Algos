from typing import List

class KMPAlgorithm:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.lps = self._compute_lps(pattern)

    def _compute_lps(self, pattern: str) -> List[int]:
        """
        Computes the Longest Prefix Suffix (LPS) array for the pattern.
        LPS array is used to skip characters while matching.
        """
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, text: str) -> List[int]:
        """
        Searches for occurrences of the pattern in the given text.
        Returns a list of start indices of the pattern in the text.
        """
        m = len(self.pattern)
        n = len(text)
        lps = self.lps

        indices = []
        i = 0  # index for text
        j = 0  # index for pattern

        while i < n:
            if self.pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                indices.append(i - j)
                j = lps[j - 1]
            elif i < n and self.pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return indices

