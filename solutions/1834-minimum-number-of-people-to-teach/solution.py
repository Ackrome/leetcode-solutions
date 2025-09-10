class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        been = set()
        for u,v in friendships:
            ui,vi = u-1,v-1

            if len(set(languages[ui]) & set(languages[vi]))==0:
                been.add(ui)
                been.add(vi)
        
        if not been:
            return 0


        counter = [0] * (n+1)
        for id in been:
            for lang in languages[id]:
                counter[lang]+=1
        return len(been) - max(counter)
