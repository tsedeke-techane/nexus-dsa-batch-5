class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        target = "01"
        cnt = sum(s[i] != target[i % 2] for i in range(n))
        ans = min(cnt, n - cnt)

        for i in range(n):
            cnt -= s[i] != target[i % 2]
            cnt += s[i] != target[(i + n) % 2]
            ans = min(ans, cnt, n - cnt)
        return ans