"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        # Thai number words and units
        thaiNum = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        unit = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        # Edge case handling
        if number < 0 :
            return "number can not less than 0"
        elif number > 10_000_000:
            return "number can not less than 0 and more than 10,000,000"
        
        # Convert number to Thai text
        thaiText = ""
        numberInput = list(map(int, str(number)))  # Convert number to list of digits
        length = len(numberInput)
        unit = unit[:length]  # Slice unit list based on the length of the number
        unit = unit[::-1]  # Reverse unit list for processing from lowest to highest place

        for idx, num in enumerate(numberInput):  # Enumerate over digits and their positions
            current = length - idx
            numThai = thaiNum[num]
            
            if num == 0:
                continue
            
            # Handle special cases for Thai number formatting
            if num == 2 and current % 6 == 2:  # Special case for '2' in tens place
                numThai = "ยี่"
            elif num == 1 and current % 6 == 2:  # Special case for '1' in tens place
                numThai = ""
            elif num == 1 and current % 6 == 1 and current != length:  # Special case for '1' in units place (not the most significant digit)
                numThai = "เอ็ด"
            elif num == 1 and current == 1 and length > 1:  # Special case for '1' in most significant digit
                numThai = ""
            
            # Handle numbers beyond hundreds, avoiding "เอ็ด" if it is not needed
            if current > 3 and (num != 1 or length == 1):
                thaiText += numThai + unit[idx]
            else:
                thaiText += numThai + unit[idx]

        return thaiText

