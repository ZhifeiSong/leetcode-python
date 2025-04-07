class Solution:
    def isInteger(self, s: str) -> bool:
        if len(s) == 0:
            return False
        if len(s) == 1 and (s[0] == '+' or s[0] == '-'):
            return False
        if s[0] not in "-+0123456789":
            return False
        for i in range(1, len(s)):
            if s[i] < '0' or s[i] > '9':
                return False
        return True

    def containsDot(self, s: str) -> bool:
        for c in s:
            if c == '.':
                return True
        return False

    def isNumber(self, s: str) -> bool:
        if len(s) == 1:
            return '0' <= s[0] <= '9'  # potentially could simplify the code to be s[0].isnumeric()
        c, n = 0, 1
        while n < len(s):
            if s[c] not in "+-.eE0123456789" or s[0] in "eE":
                return False
            else:
                if s[c] == '-' or s[c] == '+':
                    if (s[n] < '0' or s[n] > '9') and s[n] != '.':
                        return False
                    if s[n] == '.' and n == len(s) - 1:
                        return False
                elif s[c] == '.':
                    if s[n] < '0' or s[n] > '9' and s[n] not in "eE":
                        return False
                    if self.containsDot(s[n:]):
                        return False
                elif s[c] == 'e' or s[c] == 'E':
                    return self.isInteger(s[n:])
                elif '0' <= s[c] <= '9':
                    if (s[n] < '0' or s[n] > '9') and s[n] not in ".eE":
                        return False
                    if s[n] in "eE":
                        return self.isInteger(s[n + 1:])
                c += 1
                n += 1
        return True

    def isNumber_leetCode(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit


solution = Solution()
assert solution.isNumber('46.e3') is True
assert solution.isNumber(".1.") is False
assert solution.isNumber("-+3") is False
assert solution.isNumber("+6e-1") is True
assert solution.isNumber('.e1') is False
assert solution.isNumber('+.E3') is False

