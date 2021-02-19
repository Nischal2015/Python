class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 2
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
        print(f"The restaurant has served {self.number_served} customers.\n")
        
    def open_restaurant(self):
        print("The restaurant is open.")
        
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self, served_number):
        self.number_served += served_number