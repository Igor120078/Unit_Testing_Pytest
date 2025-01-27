from typing import List



class ShoppingCart:
    def __init__(self, max_size: int) -> None:
        self.items: List[str] = []
        self.max_size = max_size

    def add(self, item: str) -> None:
        if self.get_size() == self.max_size:
            raise OverflowError("Cannot add more items")
        self.items.append(item)

    def get_size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items

    def get_total_price(self, price_map) -> float:
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price

