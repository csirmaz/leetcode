class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        state = 'PRE'
        innum = False
        out = 0
        vmax = 2**31-1
        for i in range(len(s)):
            c = s[i]
            if c == ' ':
                if state != 'PRE': break
                continue
            if c == '+':
                if state != 'PRE': break
                state = 'SIGN'
                continue
            if c == '-':
                if state != 'PRE': break
                state = 'SIGN'
                neg = True
                continue
            if c >= '0' and c <= '9':
                state = 'NUM'
                out *= 10
                out += ord(c)-ord('0')
                if neg:
                    if out > vmax+1: return -(vmax+1)
                else:
                    if out > vmax: return vmax
                continue
            break
        if neg: return -out
        return out
