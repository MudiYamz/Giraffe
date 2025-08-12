print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# Input and data types
user_prompt = "What is your name? "
name_1 = input(user_prompt)
print("Welcome " + name_1)

user1_prompt = "Enter 3 things you do everyday "
print(user1_prompt)
todo1 = input("Activity 1: ")
todo2 = input("Activity 2: ")
todo3 = input("Activity 3: ")

todos = (todo1, todo2, todo3, "well I hope you included sleep to your list.")
print(todos)

TV_Show = input("What is your favourite TV Show? ")
print("I love " + TV_Show)
birth_year = input("What is your birth year? ")
age = 2025 - int(birth_year)
print(age)

print("Type any two whole numbers")
number1 = int(input("First: "))
number2 = int(input("Second: "))
print("Remember the sum: " + str(number1 + number2))

course = 'Python for beginners'
print(course.upper())
print(course.title())
print(course.lower())
print("What is the programming language position of 'y' in the course title:")
print(course.find('y'))
print("Replacing 'for' with '4' in the sentence:")
print(course.replace('for', '4'))
print("Is the word 'Python' in the sentence:")
print("Python" in course)
print("This is known as a boolean expression; either True or False")

temperature = int(input("\nWhat is today's temperature (Type temperature and get ready for a lot of jargon): "))

#For loops and conditionals
if temperature > 30:
    print("Its a hot day")
    print("Drink plenty of water")
elif temperature > 20:  # (20, 30)
    print("It's a nice day")
    print("Take the scenic route")
elif temperature > 10:  # (10, 20)
    print("It's a cold day")
    print("Wear a jacket")
elif temperature > -5:  # (-5, 10)
    print("It's Freezing")
    print("Wear a puffer jacket\t\n")

print("System idols:")
idol_1 = "My idol has always been Uwa"
print(idol_1)
print("Replacing 'Uwa' with 'Mudi'")
new_idol_1 = idol_1.replace("Uwa", "Mudi")
print(new_idol_1)
uwa_count = idol_1.count("Uwa")
print(uwa_count)
mudi_count = new_idol_1.count("Mudi")
print(mudi_count)

print("\nTop 3 magicians of all time")
magicians = ["harry", "dynamo", "copperfield"]
for magician in magicians:
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
print("\nNigeria will be added to the list")
travel_list.append("nigeria")
print(travel_list)
print("\nShow last entry on the list")
print(travel_list[-1].title(), "\n")

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
    squares.append(value ** 2)  # creating a loop to add a squared range of numbers
print(squares, "\n\n")

players = ["don", "michael", "john", "richard", "okemute", "frederick"]
print(players)
for player in players[:3]:  # looping through a sliced list
    print(player.title(), "\n")

print("The first 10 number cubed")
cubed_numbers = [value ** 3 for value in range(1, 11)]  # list comprehension for cubed values
print(cubed_numbers)

my_food = ["pizza", "falafel", "mushrooms", "dates", "chips"]
friend_foods = my_food[:]  # COPYING LIST using a slice allows you to make unique changes to both lists.

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
print('\n', car.lower() == "audi")  # making a case-insensitive to check the condition.
print(car)  # The value stored 'Audi' not affected by conditional test.
# This can be used to compare usernames and make sure no similar usernames e.g., John, john

requested_toppings = ['mushrooms', 'pineapple', 'onions']
print('\n', requested_toppings)
print("\nAre mushrooms in the requested toppings?")  # Checking whether a value is in a list.
print('mushrooms' in requested_toppings)
print("\nIs there ham in in the requested toppings?")
print('ham' in requested_toppings)
for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("Sorry we are out of mushrooms")  # If there is a condition to a value within the loop.
    else:
        print("Adding " + requested_topping + ".")

requested_toppings = []  # Checking that a list is not empty

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your Pizza!")
else:
    print("Are you sure you want a plain pizza")

print("\nFinished making your Pizza")

banned_users = ['John', 'Andrew', 'James', 'Neo']
user = 'Chanel'

if user not in banned_users:  # Checking whether a value is not in a list, so a user sees a message.
    print("\n", user.title() + ",you can post a response if you wish.")

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
# Using multiple lists.
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("\nAdding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your Pizza!")

usernames = ["admin", "joy", "mudi", "jonathan", "tosin"]

for username in usernames:
    if username == "admin":
        print("\nHello Admin, would you like a status report")
    else:
        print("Hello " + username + ", thank you for logging in.")

usernames = []

if usernames:
    for username in usernames:
        print("Hello " + username + ".")
else:
    print("\nWe need to get some users")

current_users = ["ajayi", "benedict", "joshua", "hamza", "blaise"]

new_users = ["Hamza", "joshua", "james", "timothy"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("\n", new_user + " already exist; Enter new username.")
    else:
        print(new_user + " :this username is available.")

ordinal_numbers = list(range(1, 10))

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print("1st")
    elif ordinal_number == 2:
        print("2nd")
    elif ordinal_number == 3:
        print("3rd")
    else:
        print(str(ordinal_number) + "th")


#Functions
def number_squared(number, power):
    print(number ** power)


number_squared(5, 3)


def number_args(*number):
    print(number[0] * number[1])


number_args(5, 6, 1, 2, 8)

args_tuple = (5, 6, 1, 2, 8)


def number_jags(*number):
    print(number[0] * number[1])


number_jags(*args_tuple)


# Also know how to use the keyword argument.

def number_square(**number):
    print("My number is: " + number["integer"])


number_square(integer='2309')


def greet(first_name, last_name):  #
    print(f"Hi {first_name} {last_name}")
    print("hope you are doing good today")


greet("Mudi", "Yamu")

alien_0 = {'color': 'green', 'points': 5}  # Dictionary use, key-value pair
print(alien_0['color'])  # color is the key: and its value is green

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x-position'] = 0  # Adding a key-value pair to the dictionary
alien_0['y-position'] = 25
print(alien_0)

#List Comprehension
prices = [10, 38, 40, 58, 62]
halved = []

for price in prices:
    half_price = price / 2
    halved.append(half_price)

print(halved)

prices = [10, 38, 40, 58, 62]

halved = [price / 2 for price in prices]
print(halved)

flights = ["1122", "5788", "0044"]

codes_a = ["BA" + flight for flight in flights]
print(codes_a)

codes_b = []
for flight in flights:
    code = "BA" + flight
    codes_b.append(code)

print(codes_b)

miles = [100, 57, 40, 20]

km = [value * 1.609 for value in miles]

print(km)

answers = [False, True, True]


#Functions

def greet_user(name):
    """Display a simple greeting"""
    print("\nHello, " + name.title() + "!")


greet_user('John')


def display_message():
    """Learning functions in Python"""
    print("\nI am learning Python.")


display_message()


def favorite_book(book):
    """Name of my favorite book"""
    print("\n\tMy favorite book is " + book.title() + ".")


favorite_book('alice in wonderland')

# Nesting: alist of dictionaries
alien_1 = {'color': 'blue', 'points': 25}
alien_2 = {'color': 'blue', 'points': 27}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# Make an empty list for storing aliens.
anders = []

# Making 30 green aliens.
for ander_number in range(0,30):
    new_ander = {'color': 'black', 'points': 12, 'speed': 'slow'}
    anders.append(new_ander)
    # show first 5 aliens
    for ander in anders[:5]:
        print(anders)

print("...")

# Multiple function calls
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'roger')
describe_pet('dog', 'georger')
