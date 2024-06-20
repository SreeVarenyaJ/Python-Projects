class Restaurant:
    def __init__(self, name, location, menu):  # Corrected to use double underscores
        self.name = name
        self.location = location
        self.menu = menu  

    def get_menu(self):
        return self.menu

    def is_dish_available(self, dish_name):
        return dish_name in self.menu

class Customer:
    def __init__(self, name):  # Corrected to use double underscores
        self.name = name
        self.orders = []  
        self.total_amount = 0
        self.payment_method = None

    def place_order(self, restaurant, dish_name):
        if restaurant.is_dish_available(dish_name):
            self.orders.append(dish_name)
            self.total_amount += restaurant.menu[dish_name]
        else:
            print(f"Sorry, {dish_name} is not available at {restaurant.name}")

    def choose_payment_method(self, method):
        self.payment_method = method

    def get_order_summary(self):
        return {
            'Customer': self.name,
            'Orders': self.orders,
            'Total Amount': self.total_amount,
            'Payment Method': self.payment_method
        }

# Example usage
restaurant1 = Restaurant("Paradise", "F2", {"Biriyani": 210, "Roti": 30, "Palak Paneer": 212})
restaurant2 = Restaurant("Green house", "Svn", {"Fried Rice": 115, "Jeera Rice": 110, "Gravy": 112})

customer1 = Customer("Tom")
customer1.place_order(restaurant1, "Biriyani")
customer1.place_order(restaurant1, "Roti")
customer1.place_order(restaurant2, "Gravy")
customer1.choose_payment_method("Credit Card")

print(customer1.get_order_summary())
