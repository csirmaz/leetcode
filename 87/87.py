
# 87. Scramble String

class Solution:

    known = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        ln = len(s1)

        if ln == 1: return False

        if ln == 2:
            s2rev = s2[1] + s2[0]
            return (s2rev == s1)

        key = s1+"|"+s2
        is_known = self.known.get(key)
        # print(f"s1={s1} s2={s2} kn={is_known}")
        if is_known is not None: return is_known

        # Check for each possible split position
        for sp in range(1, ln):

            s21 = s2[0:sp]
            s22 = s2[sp:ln]
            if s1[0] in s21 and s1[sp] in s22: # Shortcut
                # Check for no swap case
                if self.isScramble(s1[0:sp], s21) and self.isScramble(s1[sp:ln], s22):
                    self.known[key] = True
                    return True

            s21 = s2[0:ln-sp]
            s22 = s2[ln-sp:ln]
            if s1[0] in s22 and s1[sp] in s21: # Shortcut
                # Check for swapped case
                if self.isScramble(s1[0:sp], s22) and self.isScramble(s1[sp:ln], s21):
                    self.known[key] = True
                    return True

        self.known[key] = False
        return False
