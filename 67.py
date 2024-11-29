class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        result = ""
        carry = 0

        for i in range(max(len(a), len(b))):
            temp_a = int(a[i]) if i < len(a) else 0
            temp_b = int(b[i]) if i < len(b) else 0

            total = temp_a + temp_b + carry
            result = str(total % 2) + result
            carry = total // 2

        if carry:
            result = str(carry) + result

        return result
