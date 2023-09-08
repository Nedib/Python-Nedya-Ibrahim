food_items = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]
for itens in food_items:
    print(day)

weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]
for day in weekdays:
    print(day)


# Ensure that the number of food items matches the number of weekdays
if len(food_items) == len(weekdays):
    food_menu = dict(zip(weekdays, food_items))

    # Print the food menu
    for day, food in food_menu.items():
        print(f"{day}: {food}")
else:
    print("The number of food items does not match the number of weekdays.")
