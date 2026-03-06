class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def get_max(target):
            max_len = current = 0
            for char in s:
                if char == target:
                    current += 1
                    max_len = max(max_len, current)
                else:
                    current = 0
            return max_len

        return get_max("1") > get_max("0")