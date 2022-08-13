from restaurant1 import Restaurant

# Quuestion 9-10. Imported Restaurant
restaurant = Restaurant('apetito', 'african')
print(f"The restaurant name is {restaurant.name.title()}.")
print(f"The restaurant Cuisine type is {restaurant.cuisine.title()}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()