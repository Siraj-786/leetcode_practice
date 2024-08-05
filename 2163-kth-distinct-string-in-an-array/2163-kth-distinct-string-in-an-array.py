class Solution:
    def kthDistinct(self, arr, k):
        distinct_strings = set()
        duplicate_strings = set()

        # First pass: Identify distinct and duplicate strings
        for s in arr:
            # If the string is already in duplicate_strings, skip further processing
            if s in duplicate_strings:
                continue
            # If the string is in distinct_strings, it means we have seen it before,
            # so move it to duplicate_strings
            if s in distinct_strings:
                distinct_strings.remove(s)
                duplicate_strings.add(s)
            else:
                distinct_strings.add(s)

        # Second pass: Find the k-th distinct string
        for s in arr:
            if s not in duplicate_strings:
                # Decrement k for each distinct string encountered
                k -= 1
            # When k reaches 0, we have found the k-th distinct string
            if k == 0:
                return s

        return ""