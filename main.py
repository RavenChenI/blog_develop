from typing import List


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        str_num = str(N)
        flag = len(str_num)

        for i in range(len(str_num) - 1, 0, -1):
            if str_num[i - 1] > str_num[i]:
                flag = i

                str_num = str_num[:i-1] + str(int(str_num[i - 1]) - 1) + str_num[i:]
                print(str_num)

        for i in range(flag, len(str_num)):
            str_num = str_num[:i] + '9'

        return int(str_num)

# Example usage:
ratings = 1010
solution = Solution()
result = solution. monotoneIncreasingDigits(ratings)
print(result)

s = '-1'
print(str(int(s)))