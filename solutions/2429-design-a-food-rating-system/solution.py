from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_foods = defaultdict(SortedSet)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            # В SortedSet храним (-рейтинг, название) чтобы:
            # 1. Высший рейтинг был первым (по отрицательному значению)
            # 2. При равенстве — лексикографически меньшее название (т.к. строки сравниваются по умолчанию)
            self.cuisine_to_foods[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        old_rating = self.food_to_rating[food]
        
        # Удаляем старую запись
        self.cuisine_to_foods[cuisine].discard((-old_rating, food))
        
        # Обновляем рейтинг
        self.food_to_rating[food] = newRating
        self.cuisine_to_foods[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Первый элемент в SortedSet — с наивысшим приоритетом
        return self.cuisine_to_foods[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
