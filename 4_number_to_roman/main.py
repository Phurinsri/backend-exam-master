"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        list_roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        dict_roman = {  'M': 1000,
                        'D': 500,
                        'C': 100,
                        'L': 50, 
                        'X': 10, 
                        'V': 5, 
                        'I': 1  }
        output = ""
        if number < 0 :
            return 'number can not less than 0'
        
        for index, roman in enumerate(list_roman):
            roman_value = dict_roman[roman]
            num_token = number//roman_value
            print(num_token)

            if index != 0 and num_token == 4:
                print('in')
                if len(output) > 0 and output[-1] == list_roman[index-1]:
                    output = output[:-1] + roman + list_roman[index-2]
                else:
                    output = roman + list_roman[index-1]
            else:
                print('out')
                for i in range(num_token):
                    output += roman
            number -= num_token*roman_value

        return output
        
# number = int(input())
# s = Solution()
# print(s.number_to_roman(number))