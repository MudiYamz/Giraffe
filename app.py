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
elif temperature > -5:  # (-5, 10)
    print("It's Freezing")
    print("Wear a puffer jacket\t\n")

idol_1 = "My idol has always been Uwa"
print(idol_1)
new_idol_1 = idol_1.replace("Uwa", "mudi")
print(new_idol_1)
uwa_count = idol_1.count("Uwa")
print(uwa_count)

magicians = ["harry", "dynamo", "copperfield"]
for magician in magicians:
    print("Top 3 magicians of all time\t\n")
    print(magician)

travel_list = ["Japan", "Barbados", "Netherlands", "Denmark", "China", "Jamaica"]
print("\nList countries you would like to visit")
print(travel_list)
print("\nList to be sorted alphabetically and back to original arrangement")
print(sorted(travel_list))
print(travel_list)
print("\nThe list will replace Jamaica for Morocco")
travel_list[-1] = "Morocco"
print(travel_list)




