character_name = "John"
character_age = "35"

print("John")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")


print("There once was a man named George")
print("he was 70 years old")
print("he really liked his name George")
print("but didn't like being 70 years old")


user_prompt = "What is your name? "
name_1 = input(user_prompt)
print(name_1)

user1_prompt = "Enter 3 things you do everyday "
print(user1_prompt)
todo1 = input("Activity 1: ")
todo2 = input("Activity 2: ")
todo3 = input("Activity 3: ")

todos = (todo1, todo2, todo3, " well I hope you included sleep to your list.")
print(todos)

TV_Show = input("What is your favourite TV Show? ")
print("I love " + TV_Show)
birth_year = input("What is your birth year? ")
age = 2025 - int(birth_year)
print(age)

print("Type any two whole numbers")
number1 = int(input("First: "))
number2 = int(input("Second: "))
print(number1 + number2)
print("Remember the sum: " + str(number1 + number2))

course = 'Python for beginners \t\n'
print(course.upper())
print(course.title())
print(course.lower())
print("Position of 'y' in the course title")
print(course.find('y'))
print(course.replace('for', '4'))
print("Python" in course)

temperature = int(input("What is today's temperature: "))

if temperature > 30:
    print("Its a hot day")
    print("Drink plenty of water")
elif temperature > 20:   # (20, 30)
    print("It's a nice day")
    print("Take the scenic route")
elif temperature > 10:   # (10, 20)
    print("It's a cold day")
    print("Wear a jacket")
elif temperature > -5:  # (-5, 10)
    print("It's Freezing")
    print("Wear a puffer jacket\t\n")

idol_1 = "My idol has always been Uwa"
print(idol_1)
new_idol_1 = idol_1.replace("Uwa", "Mudi")
print(new_idol_1)
uwa_count = idol_1.count("Uwa")
print(uwa_count)

magicians = ["harry", "dynamo", "copperfield"]
for magician in magicians:
    print("Top 3 magicians of all time")
    print(magician, "\t\n")

travel_list = ["japan", "barbados", "netherlands", "denmark", "china", "jamaica"]  # creating list and for looping list
for destination in travel_list:
    print(destination)
    print(destination.title() + " , that's a lovely destination")
print("\nList countries I would like to visit")
print(travel_list)
print("\nList to be sorted alphabetically and back to original arrangement")
print(sorted(travel_list))
print(travel_list)
print("\nThe list will replace Jamaica for Morocco")
travel_list[-1] = "morocco"
print(travel_list)
print("\nThe list will add Nigeria")
travel_list.append("nigeria")
print(travel_list)
print("\nShow last entry on the list")
print(travel_list[-1], "\n")

pizzas = ["margarita", "pepperoni", "vegan paradise"]
for pizza in pizzas:
    print(pizza, "\n")
    print("I like " + pizza.title() + " pizza.""\n")  # looping a list and capitalising the first letters
print("I love so many different types of pizza\n", "I love pizza\n", "I love pizza\n")

animals = ["giraffe", "bear", "lion"]
for animal in animals:
    print(animal)
    print("A " + animal + " will make a great pet\n")  # looping a list with an added sentence
print("Any of these animals will make a great pet")

print("Number range from 1-101")
trill_figures = list(range(1, 102))
print(trill_figures, "\n")

fig = [1, 2, 3, 4]
print(fig)
print(min(fig))
print("\t", max(fig))
print("\t\t", sum(fig), "\n")

fig_figures = list(range(2, 102, 2))  # creating a range and further defining the numeric pattern
print(fig_figures)

squares = []
for value in range(1, 21):
    squares.append(value**2)  # creating a loop to add a squared range of numbers
print(squares)

print(squares)
players = ["don", "michael", "john", "richard", "okemute", "frederick"]
print(players)
for player in players[:3]:  # looping through a sliced list
    print(player.title(), "\n")

cubed_numbers = [value**3 for value in range(1, 11)]  # list comprehension for cubed values
print(cubed_numbers)
print("The first 10 ")

my_food = ["pizza", "falafel", "mushrooms", "dates", "chips"]
friend_foods = my_food[:]  # COPYING LIST using a slice allows you to make unique changes to both list.

print("My favorite foods are: ")
print(my_food)

print("\nMy friends favorite foods are: ")
print(friend_foods)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("\nWorking with Tuples")
angles = (300, 45, 90)
print("Original angles")
for angle in angles:
    print(angle)

angles = (400, 50, 95)
print("\nModified angles")
for angle in angles:
    print(angle)

matrix = [[0, 1], [2, 3]]

Basic_foods = ("rice", "beans", "chips", "brocolli", "spinach")
print("\nBuffet food list")
for Basic_food in Basic_foods:
    print(Basic_food.title())

Basic_foods = ("garri", "beans", "wedges", "brocolli", "hummus")
print("\nModified Buffet food list")
for Basic_food in Basic_foods:
    print(Basic_food.title())

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print('\n', car.upper())  # Ability to single out an item in list and uppercase.
    else:
        print('\n', car.title())

car = "Audi"
print('\n', car.lower() == "audi")  # making case-insensitive in order to check the condition.
print(car)  # The value stored 'Audi' not affected by conditional test.
# This can be used to compare usernames and make sure no similar usernames e.g. John, john

requested_toppings = ['mushrooms', 'pineapple', 'onions']
print('\n', requested_toppings)
print("\nAre mushrooms in the requested toppings?")
print('mushrooms' in requested_toppings)
print("\nIs there ham in in the requested toppings?")
print('ham' in requested_toppings)
