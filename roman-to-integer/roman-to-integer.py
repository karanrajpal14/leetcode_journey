class Solution:
    def romanToInt(self, s: str) -> int:
        total_value = prev_value = 0
        
        symbol_value_map = {
            'M' : 1000,
            'CM' : 900,
            'D' : 500,
            'CD' : 400,
            'C' : 100,
            'XC' : 90,
            'L' : 50,
            'XL' : 40,
            'X' : 10,
            'IX' : 9,
            'V' : 5,
            'IV' : 4,
            'I' : 1
        }
        
        for char in reversed(s):
            curr_value = symbol_value_map[char]
            
            if curr_value < prev_value:
                total_value -= curr_value
            else:
                total_value += curr_value
            
            prev_value = curr_value
        
        return total_value
        