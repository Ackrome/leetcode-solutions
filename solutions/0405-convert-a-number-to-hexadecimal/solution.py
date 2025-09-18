class Solution:
    def toHex(self, num: int) -> str:
        return str(hex((num + (1 << 32)) % (1 << 32)))[2:]
