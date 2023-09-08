#Food menu
food_items =  ["Vegetarian lasagna", "Spaghetti", "Fish", "Vegetable soup", "Pancakes"]
#weekdays
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#Ensure that the number of food items matches the number of weekdays
if len(food_items) == len(weekdays): 
    food_menu = dict(zip(weekdays, food_items))

    #print the food menu
    for day, food in food_menu.items():
        print(f"{day}: {food}")
else:
    print("The number of food items does not match the number of weekdays. ")        
