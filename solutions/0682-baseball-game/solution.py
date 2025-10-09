class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = [0,0]
        for i in range(len(operations)):
            try:
                scores.append(int(operations[i]))
            except:
                if operations[i] == '+':
                    scores.append(scores[-1]+scores[-2])
                elif operations[i] == 'D':
                    scores.append(scores[-1]*2)
                else:
                    del scores[-1]
        return sum(scores)
