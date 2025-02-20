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
add_numbers = print(number1 + number2)
print("Remember the sum: " + add_numbers)

course = 'Python for beginners '
print(course.upper())
print(course.find('y'))
print(course.replace('for', '4'))
print("Python" in course)

temperature = float(input("What is today's temperature: "))

if temperature > 30:
    print("Its a hot day")
    print("Drink plenty of water")
elif temperature > 20:   # (20, 30)
    print("It's a nice day")
    print("Take the scenic route")
elif temperature > 10:   # (10, 20)
    print("It's a cold day")
    print("Wear a jacket")

magicians = ['alice', 'david', 'chris']
print(magicians.title(0))





