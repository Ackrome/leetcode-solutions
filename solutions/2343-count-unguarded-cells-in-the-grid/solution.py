from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        """
        A more optimized solution with O(m * n) time complexity.
        """
        # Sets for O(1) lookups
        walls_set = {tuple(w) for w in walls}
        guards_set = {tuple(g) for g in guards}
        
        # A set to store the coordinates of all guarded cells
        guarded_cells = set()

        # Sweep through each row
        for r in range(m):
            # Left to right
            is_guarded = False
            for c in range(n):
                pos = (r, c)
                if pos in guards_set:
                    is_guarded = True
                elif pos in walls_set:
                    is_guarded = False
                elif is_guarded:
                    guarded_cells.add(pos)
            
            # Right to left
            is_guarded = False
            for c in range(n - 1, -1, -1):
                pos = (r, c)
                if pos in guards_set:
                    is_guarded = True
                elif pos in walls_set:
                    is_guarded = False
                elif is_guarded:
                    guarded_cells.add(pos)

        # Sweep through each column
        for c in range(n):
            # Top to bottom
            is_guarded = False
            for r in range(m):
                pos = (r, c)
                if pos in guards_set:
                    is_guarded = True
                elif pos in walls_set:
                    is_guarded = False
                elif is_guarded:
                    guarded_cells.add(pos)
            
            # Bottom to top
            is_guarded = False
            for r in range(m - 1, -1, -1):
                pos = (r, c)
                if pos in guards_set:
                    is_guarded = True
                elif pos in walls_set:
                    is_guarded = False
                elif is_guarded:
                    guarded_cells.add(pos)
        
        # Total cells minus obstacles and guarded cells
        return m * n - len(walls_set) - len(guards_set) - len(guarded_cells)
