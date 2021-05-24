# Basic Trie node
class TrieNode:
    
    def __init__(self, char):
        self.char = ""
        self.children = {}
        self.is_end_of_word = False

class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        Initialized with empty string as it's the root
        """
        self.root = TrieNode("")
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        We traverse from the root and insert the chars of a word
        """
        node = self.root
        
        # If the char is already present in the children,
        # then we just move along to the next node
        # else we create a new node and append it to the end of the tree
        # once we are done we mark the end of the word
        for char in word:
            if char in node.children:
                node = node.children.get(char)
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        node.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        """
        To search for a word, we start from the root
        and traverse down the tree until the end of the word
        We then return the end of word flag
        """
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children.get(char)
            else:
                return False
        
        return node.is_end_of_word
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        
        for char in prefix:
            if char in node.children:
                node = node.children.get(char)
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)