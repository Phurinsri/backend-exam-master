"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        # Check if the list is empty
        if not numbers:
            return "list can not be blank"
        
        # Initialize the index and value of the maximum element
        max_index = 0
        max_value = numbers[0]
        
        # Iterate through the list starting from the second element
        for index in range(1, len(numbers)):
            if numbers[index] > max_value:
                max_value = numbers[index]
                max_index = index
        
        return max_index
