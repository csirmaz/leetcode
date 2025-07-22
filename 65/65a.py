
# https://leetcode.com/problems/valid-number/description/

class Solution:

    def isNumber(self, s: str) -> bool:
        state = 'begin'
        was_num = False

        for c in s:
            if state == 'num': was_num = True

            if c in "0123456789":
                if state == 'begin': state = 'num'; continue
                if state == 'sign': state = 'num'; continue
                if state == 'num': state = 'num'; continue
                if state == 'dec': state = 'dec_num'; continue
                if state == 'dec_num': state = 'dec_num'; continue
                if state == 'exp': state = 'exp_num'; continue
                if state == 'exp_sign': state = 'exp_num'; continue
                if state == 'exp_num': state = 'exp_num'; continue
                return False

            if c in "+-":
                if state == 'begin': state = 'sign'; continue
                if state == 'exp': state = 'exp_sign'; continue
                return False

            if c == '.':
                if state == 'begin': state = 'dec'; continue
                if state == 'sign': state = 'dec'; continue
                if state == 'num': state = 'dec'; continue
                return False

            if c in "eE":
                if state == 'num': state = 'exp'; continue
                if state == 'dec_num': state = 'exp'; continue
                if state == 'dec' and was_num: state = 'exp'; continue
                return False

            return False

        if state == 'num': return True
        if state == 'dec': return was_num
        if state == 'dec_num': return True
        if state == 'exp_num': return True
        return False

