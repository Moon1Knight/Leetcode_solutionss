class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        strs = []
        for x in range(1, n + 1):
            strs.append(str(x))
        return [int(s) for s in sorted(strs)]