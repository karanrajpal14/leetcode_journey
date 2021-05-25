from collections import defaultdict
import re

"""
    The first step here is to sanitize the string.
    We do this by lowering the case and then removing
    all the punctuation.
    
    Once that is done, we iterate over the words and count
    the frequency of each word. Yes, we could use Counter
    here but where is the fun in that?
    
    Once we have the frequencies, all that's left is to return
    the max of this dict. While there are many ways to do this,
    here we will rely on using the "key" arg of max.
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        frequency = defaultdict(int)
        
        cleaned_paragraph = re.sub(r'\W+', ' ', paragraph).lower().split()
        
        for word in cleaned_paragraph:
            if word not in banned:
                frequency[word] += 1
            
        return max(frequency, key=frequency.get)