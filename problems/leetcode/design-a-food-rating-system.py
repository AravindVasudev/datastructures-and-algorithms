# https://leetcode.com/problems/design-a-food-rating-system/
from dataclasses import dataclass

@dataclass
class Food:
    name: str
    rating: int

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.name < other.name

        return self.rating > other.rating


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cusineToFoodHeap = defaultdict(list)
        self.foodToRating = {}
        self.foodToCuisine = {}

        for i in range(len(foods)):
            self.foodToRating[foods[i]] = ratings[i]
            self.foodToCuisine[foods[i]] = cuisines[i]

            heapq.heappush(
                self.cusineToFoodHeap[cuisines[i]], Food(foods[i], ratings[i]))
        

    def changeRating(self, food: str, newRating: int) -> None:
        self.foodToRating[food] = newRating

        cuisine = self.foodToCuisine[food]
        heapq.heappush(self.cusineToFoodHeap[cuisine], Food(food, newRating))

        

    def highestRated(self, cuisine: str) -> str:
        highest = self.cusineToFoodHeap[cuisine][0]
        while self.foodToRating[highest.name] != highest.rating:
            heapq.heappop(self.cusineToFoodHeap[cuisine])
            highest = self.cusineToFoodHeap[cuisine][0]

        return highest.name
