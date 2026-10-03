class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []
        zeroes = 0
        positives_once = set()
        positives_twice = set()
        negatives_once = set()
        negatives_twice = set()
        for i, v in enumerate(nums):
            if v<0:
                if v in negatives_once:
                    negatives_twice.add(v)
                else:
                    negatives_once.add(v)
            elif v>0:
                if v in positives_once:
                    positives_twice.add(v)
                else:
                    positives_once.add(v)
            else:
                zeroes += 1
        if zeroes >= 3:
            # i!=j && j!=k && i!=k does not guarantee that there are no duplicate triplets
            # anyway...
            out.append([0,0,0])
        if zeroes >= 1:
            for p in positives_once:
                if -p in negatives_once:
                    out.append([p,0,-p])
        for p in positives_twice:
            if -p-p in negatives_once:
                out.append([p,p,-p-p])
        for n in negatives_twice:
            if -n-n in positives_once:
                out.append([n,n,-n-n])
        for p1 in positives_once:
            for p2 in positives_once:
                if p1>p2 and -p1-p2 in negatives_once:
                    out.append([p1,p2,-p1-p2])
        for n1 in negatives_once:
            for n2 in negatives_once:
                if n1>n2 and -n1-n2 in positives_once:
                    out.append([n1,n2,-n1-n2])
        return out
