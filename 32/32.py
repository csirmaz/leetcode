class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxl = 0
        data = []
        for c in s:
            if c == '(':
                data.append(-1)
            else:
                if len(data) > 0 and data[-1] == -1:
                    data[-1] = 2
                    maxl = 2
                else:
                    data.append(-2)
        while True:
            #print(data)
            changed = False
            data2 = []
            for d in data:
                if len(data2) > 0 and d > 0 and data2[-1] > 0:
                    #print("merge")
                    data2[-1] += d
                    if data2[-1] > maxl: maxl = data2[-1]
                    changed = True
                elif len(data2) > 1 and d == -2 and data2[-1] > 0 and data2[-2] == -1:
                    #print("pair")
                    data2[-2] = data2[-1] + 2
                    if data2[-2] > maxl: maxl = data2[-2]
                    del data2[-1:]
                    changed = True
                else:
                    data2.append(d)
            #print(data2)
            if not changed:
                return maxl
            data = data2
