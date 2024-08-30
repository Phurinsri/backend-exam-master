"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        # negative input
        if number < 0:
            return "number can not be negative"

        count_zero = 0
        power_of_5 = 5

        # Count 5 in n!
        while number >= power_of_5:
            count_zero += number // power_of_5
            # condition 25 125 625 ... 
            power_of_5 *= 5

        return count_zero


# try:
#     solution = Solution()
#     number = int(input("Enter a number: "))
#     # count of tailing zero as an integer
#     print(solution.find_tailing_zeroes(number))
# except ValueError:
#     print("Invalid input")
