
# https://leetcode.com/problems/regular-expression-matching/description/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        s = '^'+s
        p = '^'+p

        pattern = []
        pstar = []
        for c in p:
            if c == '*' and len(pstar):
                pstar[-1] = True
                continue
            pattern.append(c)
            pstar.append(False)

        matrix = [[0] * len(s) for c in pattern]

        q = 1
        for pix in range(len(pattern)): # which row
            for six in range(len(s)): # which column

                if pix == 0:
                    if six == 0:
                        matrix[pix][six] = 1
                    continue

                if pstar[pix]:
                    if matrix[pix-1][six] != 0:
                        matrix[pix][six] = q
                        continue

                    if six == 0: 
                        continue
                    if six > 0 and matrix[pix][six-1] == 0: 
                        continue

                    
                    
                else:
                    if six == 0: continue
                    if matrix[pix-1][six-1] == 0: continue

                if pattern[pix] == '.' or pattern[pix] == s[six]:
                    matrix[pix][six] = q
                    q += 1


        return not not matrix[-1][-1]
