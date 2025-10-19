from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        # Use a queue for a Breadth-First Search (BFS) to explore all possible strings
        q = deque([s])
        # 'seen' stores every unique string we've encountered to avoid cycles and redundant work
        seen = {s}
        # 'ans' will keep track of the lexicographically smallest string found so far
        ans = s

        while q:
            current_s = q.popleft()

            # Compare the current string with the best answer found and update if it's smaller
            if current_s < ans:
                ans = current_s

            # --- Apply Operation 1: Add 'a' to odd-indexed digits ---
            add_list = list(current_s)
            for i in range(1, n, 2):
                add_list[i] = str((int(add_list[i]) + a) % 10)
            s_after_add = "".join(add_list)

            if s_after_add not in seen:
                seen.add(s_after_add)
                q.append(s_after_add)

            # --- Apply Operation 2: Rotate left by 'b' ---
            s_after_rotate = current_s[b:] + current_s[:b]

            if s_after_rotate not in seen:
                seen.add(s_after_rotate)
                q.append(s_after_rotate)

        return ans
