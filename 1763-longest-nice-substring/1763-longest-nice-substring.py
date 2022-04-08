class Solution:
    def longestNiceSubstring(self, s):
        subs = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        nice = filter(lambda x : set(x) == set(x.swapcase()), subs)
        return max(nice, key=len, default="")