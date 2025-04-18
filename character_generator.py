#imports
import random
import json
import os

# Method for selecting a specified race
def generate_character_wname(race_name="elf"):

    chosen_creature = ""
    for c in creatures:
        if c["race"] == race_name:
            chosen_creature = c
    #print(chosen_creature)
    chosen_personality = normalised_attribute_picker(attribute_personalities,"personality", chosen_creature)
    chosen_build = normalised_attribute_picker(attribute_build,"build", chosen_creature)
    chosen_size = normalised_attribute_picker(attribute_size,"size", chosen_creature)
    chosen_ideology = normalised_attribute_picker(attribute_ideologies, "ideology", chosen_creature)
    chosen_ruling = normalised_attribute_picker(attribute_ruling, "ruling_type", chosen_creature)
    
    # Making the return value based of traits 
    description = chosen_creature["race"] + ", " + chosen_personality + ", " + chosen_build + ", " + chosen_size + ", " + chosen_ideology + ", " + chosen_ruling

    # Debug prints
    print("Race: " + chosen_creature["race"])
    print("Attributes: ")
    print("\t Personnality: " + chosen_personality)
    print("\t Build: " + chosen_build)
    print("\t Size: " + chosen_size)
    print("\t Ideology: " + chosen_ideology)
    print("\t Ruling type: " + chosen_ruling)
    print("------------------------------------------")
    #
    
    return description
#

# function for generating a randomised creature
def generate_character():
    # Randomising Traits
    chosen_creature = random.choice(creatures)
    #print(chosen_creature)
    chosen_personality = normalised_attribute_picker(attribute_personalities,"personality", chosen_creature)
    chosen_build = normalised_attribute_picker(attribute_build,"build", chosen_creature)
    chosen_size = normalised_attribute_picker(attribute_size,"size", chosen_creature)
    chosen_ideology = normalised_attribute_picker(attribute_ideologies, "ideology", chosen_creature)
    chosen_ruling = normalised_attribute_picker(attribute_ruling, "ruling_type", chosen_creature)
    
    # Making the return value based of traits 
    description = chosen_creature["race"] + ", " + chosen_personality + ", " + chosen_build + ", " + chosen_size + ", " + chosen_ideology + ", " + chosen_ruling


    # Debug prints
    print("Race: " + chosen_creature["race"])
    print("Attributes: ")
    print("\t Personnality: " + chosen_personality)
    print("\t Build: " + chosen_build)
    print("\t Size: " + chosen_size)
    print("\t Ideology: " + chosen_ideology)
    print("\t Ruling type: " + chosen_ruling)
    print("------------------------------------------")
    #
    
    return description

#
# function in charge of making the odds for an attribute given
# sending the original list of all attributes, followed by the desired attribute name for the creature, followed by the creature dict from the json
def normalised_attribute_picker(attributes_list,attribute_name, creature):
    
    # getting the name and attributes
    #creature_name = creature["race"]
    creatures_attributes = creature["attributes"]
    
    dictionary = dict()
    creature_attribute_modifier = [""]
    
    # trying to find the attribute with the name, if not found will default to having evenly split odds
    try:
        creature_attribute_modifier = creatures_attributes[attribute_name]
    except:
        print("No attributes with the name '" + attribute_name + "' defaulting...")
    
    # changing the weight depending on race modifiers
    if creature_attribute_modifier != [""]:
        for attr in creature_attribute_modifier:
            attribute_name = attr.split(":")[0]
            attribute_value = attr.split(":")[1]
            dictionary[attribute_name] = attribute_value
    else: 
        # adding 1 to every attributes since there are no modifiers
        for attribute in attributes_list:
            dictionary[attribute] = 1

    # logic to divide the 'weight' and make the randomised pick
    total = 0
    for attr in dictionary:
        total += int(dictionary[attr])

    outcome = random.randint(1, total)
    current = 0
    return_value = ""
    for attr in dictionary: 
        if current < outcome and outcome <= int(dictionary[attr]) + current and int(dictionary[attr]) != 0:
            return_value = attr
        
        current += int(dictionary[attr])        
    
    return return_value

# initializing classes and modifiers with json file
# The attribute file must be called 'attributes.json'

# current path to be able to open from anywhere in the console
cur_path = os.path.dirname(__file__)
# Open and read the JSON file
with open(cur_path + "./JSON_FILES/attributes.json", 'r') as file:
    data = json.load(file)

# reading 'builds' from the json
try:
    attribute_build = data["builds"]
except:
    print("'Builds' got an error in formatting")

# reading 'size' from the json
try:
    attribute_size = data["sizes"]
except:
    print("'sizes' got an error in formatting")

# reading 'personalities' from the json
try:
    attribute_personalities = data["personalities"]
except:
    print("'personalities' got an error in formatting")

# reading 'ideologies' from the json
try:
    attribute_ideologies = data["ideologies"]
except:
    print("'ideologies' got an error in formatting")

# reading 'ruling_types' from the json
try:
    attribute_ruling = data["ruling_types"]
except:
    print("'ruling_types' got an error in formatting")

# reading 'creatures' from the json
try:
    creatures = data["creatures"]  
except:
    print("'creatures' got an error in formatting")

file.close()

close_program = 0
ask_again = 0
while close_program == 0:
    number=input("How many characters? \n")
    ask_again = 0
    try:
        int_number = int(number)
        if int_number <= 0:
            print("number must be positive and higher than 0")
        else:
            answer=input("Give a race? Keep blank for a randomised race or give a race from the data \n")
            for x in range(int_number):
                try:
                    if answer!="":
                        generate_character_wname(answer)
                    else:
                        generate_character()
                except:
                    print("no race found")
                    break
    except:
        print("Given value is not an integer")

    regen=input("Regenerate (blank is also yes)? Y/y, n/N \n")
    if regen=="" or regen=="y" or regen=="Y":
        close_program = 0
    elif regen=="n" or regen=="N":
        close_program = 1
    else:
        ask_again = 1 

    while ask_again == 1:
        if regen=="" or regen=="y" or regen=="Y":
            close_program = 0
            ask_again = 0
        elif regen=="n" or regen=="N":
            close_program = 1
            ask_again = 0
        else:
            ask_again = 1
            regen=input("Regenerate (blank is also yes)? Y/y, n/N \n")
        

