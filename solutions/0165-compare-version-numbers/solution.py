class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        versions1 = version1.split('.')
        versions2 = version2.split('.')
        n = len(versions1)
        m = len(versions2)
        maxnm = max(n,m)

        versions1 = list(map(int,versions1)) + [0]*(maxnm - n)
        versions2 = list(map(int,versions2)) + [0]*(maxnm - m)

        for i in range(maxnm):
            if versions1[i]>versions2[i]:
                return 1
            elif versions1[i]<versions2[i]:
                return -1
            else:
                continue
        return 0
            
