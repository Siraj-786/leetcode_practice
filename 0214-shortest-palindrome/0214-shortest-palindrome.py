class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)

        #wtf why is it accepting and that too better than 95% sol though its n^2 solution 
        

        reversed_string = s[::-1]  # Reverse the string

        # Iterate through the string to find the longest palindromic prefix
        for i in range(length):
            if s[: length - i] == reversed_string[i:]:

                return reversed_string[:i] + s
        return ""