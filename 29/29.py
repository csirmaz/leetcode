class Solution:
    def log2(self, a: int) -> int:
        l = 0
        b = 1
        while b < a:
            l += 1
            b <<= 1
        return l

    def divide(self, dividend: int, divisor: int) -> int:
        assert self.log2(1) == 0
        assert self.log2(3) == 2
        assert self.log2(5) == 3
        assert self.log2(6) == 3

        if dividend == 0: return 0
        willbeneg = 0
        if dividend < 0:
            willbeneg += 1
            dividend = -dividend
        if divisor < 0:
            willbeneg += 1
            divisor = -divisor
        if divisor > dividend: return 0

        logdend = self.log2(dividend)
        logdor = self.log2(divisor)

        l = logdend - logdor
        assert l >= 0
        o = divisor << l
        q = 0
        #print(f"dividend={dividend} divisor={divisor}")
        while True:
            #print(f"dend={dividend} o={o} l={l} q={q}")
            if o <= dividend:
                dividend -= o
                q += 1
            if l == 0: break
            l -= 1
            o >>= 1
            q <<= 1
        #print(f"*dend={dividend} o={o} l={l} q={q}")

        mx = (1<<31)-1
        if willbeneg == 1:
            if q > mx+1: return -mx-1
            return -q
        if q > mx: return mx
        return q
        
        
