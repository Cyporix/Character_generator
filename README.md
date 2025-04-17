This program can generate a character via a json file in the 'JSON_FILES' folder called 'attributes.json'.
It will generate a random race, ideoolgy, size, build and personality.

When running the program, the user will be prompted to give a number of characters to create.
After, it will ask the user if it wants to generate only one race, leaving the space blank will ignore this and generate any race.
It will then ask the user if it wants to regenerate again and going back to the first prompt. Giving 'n' or 'N' will close the application


The values and attributes can be changed in the json file heres an example:
  the categories like 'size' are made as the default option for all race if not specified
  the values in "" can be changed and other ones can be added. Any race that has no modifier for the
  category will have a chance for all the attributes in it

  Creatures can also be added, removed, or modified via the json.
  this is what a creature in the file looks like 
  { 
            "race": "gargoyle",
            "attributes": {
                "personality" : [""],
                "build" : [""],
                "size": ["short:60", "human-size:35", "tall:5"],
                "ideology": [""]
            }
  }

  removing 'personality' or build or any attributes is the same as '"personality": [""]'
  the weight for the attribute is easier to follow if all the values sum up to 100 since it will act as a percentage.
  it works with different values like ["short:1", "human-size:2", "tall:1"], in this case it will make 'human-size' 50% chance
  since it would be 2/4 chances. If there is a table of values in the attribute, the only possibilities will be that table. NOTE: You can have a type
  of an attribute only be 1 creature if desired, the attributes in the table are not required to be the same as the original 'sizes' table as they are
  intended for default settings. As such, 'gargoyle' could have ' "size": ["slender:1"] ' which would mean that it can only be slender in 'size' and it will be 
  the only race that has a custom 'size' attribute.
