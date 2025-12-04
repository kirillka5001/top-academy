class FoodStand:
    def __init__(self, name, owner, cuisine):
        self.name = name
        self.owner = owner
        self.cuisine = cuisine
        self.menu = {}  # {dish_name: (price, available_quantity)}

    def add_dish(self, dish_name, price, quantity):
        self.menu[dish_name] = (price, quantity)

    def sell_dish(self, dish_name, quantity_sold):
        if dish_name not in self.menu:
            print(f"Dish '{dish_name}' not found in menu.")
            return
        price, available = self.menu[dish_name]
        if quantity_sold > available:
            print(f"Not enough '{dish_name}' available. Available: {available}")
            return
        self.menu[dish_name] = (price, available - quantity_sold)

    def get_total_stock(self):
        return sum(qty for _, qty in self.menu.values())

# 2. Managing the Festival (Lists and Dictionaries)
# Create a list of stands
stands = [
    FoodStand("Tasty Tacos", "Alice", "Mexican"),
    FoodStand("Sushi Corner", "Bob", "Asian"),
    FoodStand("Veggie Delight", "Carol", "Vegetarian"),
    FoodStand("Pasta Paradise", "Dave", "Italian"),
    FoodStand("Curry House", "Eve", "Indian"),
]

# Add dishes to each stand
stands[0].add_dish("Taco", 5.0, 100)
stands[0].add_dish("Burrito", 7.0, 50)

stands[1].add_dish("Sushi Roll", 8.0, 80)
stands[1].add_dish("Miso Soup", 3.0, 40)

stands[2].add_dish("Veggie Salad", 4.0, 60)
stands[2].add_dish("Veggie Wrap", 5.0, 70)

stands[3].add_dish("Spaghetti", 6.0, 90)
stands[3].add_dish("Lasagna", 8.0, 40)

stands[4].add_dish("Chicken Curry", 7)
