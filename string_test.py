# def solution(s):
#     new_s = ""
#     i = 0
#     while i < len(s):
#         if s[i] == '%' and (i == len(s) - 1 or s[i + 1] != '%'):
#             new_s += '{}'
#         else:
#             new_s += s[i]
#             if s[i] == '%' and s[i + 1] == '%':
#                 i += 1  # Skip the next '%'
#         i += 1
#     return new_s
#
# # Test cases
# test_cases = [
#     "We expect the %f%% growth this week",
#     "%d%d%%-growth in products is expected quite soon",
#     "Much %%s we have here!",
#     "Nothing to insert.",
#     "New style formatting (like %s) is waay cooler than old-style (i.e. %s)",
#     "%%%%x",
#     "%%%%%d"
# ]
#
# for test_case in test_cases:
#     print(solution(test_case))

# Our goal is to find unique colors across two different baskets of fruits
# basket_1 = {"apple": "Red", "banana": "Yellow", "grape": "Purple", "pear": "Green"}
# basket_2 = {"kiwi": "Brown", "mango": "Orange", "banana": "Yellow", "apple": "Green"}
#
# # Let's create sets of colors from each basket
# colors_1 = set(basket_1.values())
# colors_2 = set(basket_2.values())
#
# print(colors_1)
#
# unique_colors = colors_1 | colors_2
# print("Unique fruit colors across both baskets:", unique_colors)

# We have our fruit baskets ready, let's look for new fruits!
# basket_X = {"banana", "kiwi", "apple", "orange"}
# basket_Y = {"banana", "cherry", "kiwi", "mango"}
#
# # TODO: Use set operations to find the total number of unique fruits in both baskets
# unique_fruits = set(basket_X | basket_Y)
# unique_fruits_count = len(basket_X | basket_Y)
# sorted_fruits = sorted(unique_fruits)
#
# # # TODO: Find the fruit that comes first in alphabetical order and print it
# # print(min(unique_fruits))
#
# # Dictionary of space suits and their weights in kg
# space_suit_weights = {'Mercury suit': 21, 'Gemini suit': 16, 'Apollo suit': 32, 'Space Shuttle suit': 50}
#
# total_weight = 0
# # TODO: Use a For Loop to calculate the total weight of all space suits
# for weight_loop in space_suit_weights:
#     print('In loop:', space_suit_weights[weight_loop])
#     total_weight += space_suit_weights[weight_loop]
# print('Total suits weight:', total_weight)

# List of planets
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#
# # A dictionary of orbit periods (days) for planets
# orbit_periods = {
#     'Mercury': 88,
#     'Venus': 225,
#     'Earth': 365,
#     'Mars': 687,
#     'Jupiter': 4333,
#     'Saturn': 10759,
#     'Uranus': 30687,
#     'Neptune': 60190,
# }
#
# # TODO: For each planet in the 'planets' list, print the name of the planet
# and its orbit period in Earth days, from the 'orbit_periods' dictionary.
# for planet_loop in planets:
#         print("The orbit period of ",planet_loop , " is ",orbit_periods[planet_loop])
#
# cadets = ["Neo", "Trinity", "Morpheus", "Agent Smith"]
# ids = [101, 102, 103, 104]
#
# for i in range(len(cadets)):
#     print('Cadet', cadets[i], 'has id', ids[i])
# for i, cadet in enumerate(cadets):
#     print('Cadet', cadet, 'has id', i)

# cosmic_objects = ['Nebula', 'Black Hole', 'Galaxy']
#
# # Use the enumerate function to iterate over cosmic_objects
# for index,listi in enumerate(cosmic_objects):
#     print("Object", index + 1, "in my list is", listi)

# stars = ["Alpha Centauri", "Betelgeuse", "Capella"]
# planets = ["Earth", "Mars", "Venus"]
#
# print("Welcome to our celestial tour! Here is a list of stars witnessed by each planet.")
# # for planet in planets:
# #     print(planet + " sees:", end=' ')
# #     for star in stars:
# #         print(star, end=', ')
# for star in stars:
#     print(star + " sees:", end=' ')
#     for planet in planets:
#         print(planet, end=', ')
#     print()
#
# # Imagine we have 3 planets in a cosmos that have different numbers of satellites.
# satellites = {'Earth': 1, 'Mars': 2, 'Neptune': 14}
#
# # TODO: For each planet, print its name along with the number of satellites it has.
#
# # TODO: For each satellite of a planet, print its order around that planet.
# # For example: Satellite 1 around Earth
# # For example: Satellite 12 around Neptune
# for satellite in satellites:
# #     print("Satellite",satellites[satellite]," around ",satellite)
# str = "world"
# summation = sum(ord(ch) for ch in str)
# print(summation)
# print(summation % 10 )
#
# text = "Hello, World!"
#
# print(text.index('World')) # prints 7
# print(text.split(", ")) # prints ["Hello", "World!"]

planet = "Earth"
orbit = "Sun"

# # TODO: Create a sentence from both of the created strings. Print the sentence.
# sent = "Planet is " + planet + " and orbit is " + orbit
# print(sent)
#
#
# # TODO: Replace the planet in the sentence with another one. Print the updated sentence
# new_sent  = sent.replace("Earth" , "Mars")
# print(sent)
# print(new_sent)

# TODO: Define the day of space travel and the planet we landed on
# day = 30
# planet = "Neptune"
#
# # TODO: Print the log message specifying when and where we've successfully landed. Use all three approaches that we've learned!
# print("Finally on Day: %d , we reahced %s" %(day,planet)) # TODO: Print the log message using strings formatting
# print("Finally on Day: {} , we reached {}".format(day,planet)) # TODO: Print the log message using strings interpolation
# print(f"Finally on Day: {day} , we reached {planet}") # TODO: Print the log message using f-strings

# # Let's create a custom table using special characters
# table = "File\tPath\nCosmosProject\tC:\\Users\\CosmoP"
# print(table)
# ----
# text = """Syntactic Structures - Noam Chomsky
# The Interpretation of Cultures - Clifford Geertz
# The Structure of Scientific Revolutions - Thomas Kuhn
# The Two Cultures - C.P. Snow"""
#
# # Turn the text into a list of lines
# lines = text.splitlines()
#
# # For each line, split the line into title and author
# catalog = []
# for line in lines:
#     title, author = line.split(" - ")
#     catalog.append((title, author))
#
# # Print the catalog
# for title, author in catalog:
#     print(f"{title}, by {author}")
# """
# Prints:
# Syntactic Structures, by Noam Chomsky
# The Interpretation of Cultures, by Clifford Geertz
# The Structure of Scientific Revolutions, by Thomas Kuhn
# The Two Cultures, by C.P. Snow
# """
# # This code takes the original text, breaks it down using the split function, and puts it back together using the join function to create a beautifully formatted catalog.

# str1 = "Hello from Mars!"
# c = str1.encode('UTF-16') # Encoding the string
# print("Encoded string: ", c)

# Create a new list and make a copy of it
# new_list = set(['Eggs', 'Jam', 'Ham'])
# copied_list = new_list.copy()
#
# print(new_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
# print(copied_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
#
# # Modifying the copied list won't affect the original list
# copied_list.remove('Ham')
# print(new_list)  # Outputs: {'Eggs', 'Ham', 'Jam'}
# print(copied_list)  # Outputs: {'Eggs', 'Jam'}

# def order_food(dish, drink):
#     # TODO: Create a string that introduces the order by combining the dish and drink parameters.
#     # The resulting string should start with "Order placed: ".
#     return_msg = f"Order placed: {dish} , {drink}"
#     return return_msg
#
# print(order_food("Pizza", "Coke"))

# def scan_planet(planet, system):
#     print('Scanning planet', planet, 'in', system)
#
# def space_mission():
#     print('Mission start.')
#     scan_planet(planet='Mars', system='Solar System')
#     scan_planet(planet='Earth', system='Solar System')
#
# adventofcode day 9

# print("Sum of three next values =",list1_nextval+list2_nextval+list3_nextval)

def double(num): # Our function that doubles the input number
    return num * 2

numbers = [1, 2, 3, 4, 5]  # Our list
doubled_numbers = list(map(double, numbers))  # Applying `double` function to each element of the list

print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]
