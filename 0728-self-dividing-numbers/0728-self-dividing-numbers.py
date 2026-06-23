from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            x = num

            while x:
                digit = x % 10

                if digit == 0 or num % digit != 0:
                    return False

                x //= 10

            return True

        ans = []

        for num in range(left, right + 1):
            if is_self_dividing(num):
                ans.append(num)

        return ans