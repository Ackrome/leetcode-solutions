class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for type, quantity in enumerate(fruits):
            if any([i>=quantity for i in baskets]):
                for basket_idx in range(len(baskets)):
                    if baskets[basket_idx]>=quantity:
                        baskets.pop(basket_idx)
                        break
                
        return len(baskets)
