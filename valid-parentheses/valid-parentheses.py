"""
    Implementing a stack out of curiosity.
    Can make do with just a plain list.
"""
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
    
class Solution:
    def isValid(self, s: str) -> bool:
        """
            Base case - there's no way we can have matching parentheses
            with odd number of chars with the constraint that we can
            not have any other characters
        """
        if len(s) % 2 != 0:
            return False
        
        opening_paren = set("([{")
        matching_paren = set([ ('(', ')'), ('[', ']'), ('{', '}') ])
        stack = Stack()
        
        """
            Here we iterate over every char in the string and see
            if any of them are opening parentheses. If they are,
            we push them to the stack.
            
            If they aren't, then we pop the last char and check if
            the pair makes a valid matching set.
        """
        
        for paren in s:
            if paren in opening_paren:
                stack.push(paren)
            else:
                if stack.size() == 0:
                    return False
                
                last_paren = stack.pop()
                
                if (last_paren, paren) not in matching_paren:
                    return False
        
        return stack.size() == 0