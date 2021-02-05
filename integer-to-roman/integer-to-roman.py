class Solution:
    def intToRoman(self, num: int) -> str:
        # Edge cases - 4, 9, 40, 90, 400, 900
        value_symbol_map = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I'
        }
        result = ""
        
        for value, symbol in value_symbol_map.items():
            while num // value != 0:
                result += symbol
                num -= value
        
        return result