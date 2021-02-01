# Implemented a Trie
class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = {}

class Solution:
    
    # Method to insert words into the Trie
    def insert(self, node, word):
        currentNode = node
        
        for char in word:
            currentNode = currentNode.children.setdefault(char, TrieNode())
        
        currentNode.isEndOfWord = True
    
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()
        
        # Insert all the words into the Trie
        for s in strs:
            self.insert(root, s)
        
        # Empty string by default
        longestCommpnPrefix = ""
        currentNode = root
        
        # Append to lcp until the number of children nodes for current node is 1
        while currentNode and not currentNode.isEndOfWord and len(currentNode.children) == 1:
            for char, node in currentNode.children.items():
                longestCommpnPrefix += char
                currentNode = node
        
        return longestCommpnPrefix