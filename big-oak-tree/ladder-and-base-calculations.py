# TO-DO: REPLACE THIS WITH A COMMENT DESCRIBING WHAT THE BELOW LINE OF CODE IS DOING
treehouse_ladder_planks = 10

# TO-DO: REPLACE THIS WITH A COMMENT DESCRIBING WHAT THE BELOW TWO (2) LINES OF CODE ARE DOING
treehouse_width = input("How wide (in feet) will the treehouse base be? ")
treehouse_length = input("How long (in feet) will the treehouse base be? ")

# Convert strings into integers
treehouse_width_integer = int(treehouse_width)
treehouse_length_integer = int(treehouse_length)

# TO-DO: REPLACE THIS WITH A COMMENT DESCRIBING WHAT THE BELOW LINE OF CODE IS DOING
treehouse_base_area = treehouse_width_integer * treehouse_length_integer

# TO-DO: REPLACE THIS WITH A COMMENT DESCRIBING WHAT THE BELOW LINE OF CODE IS DOING
treehouse_base_planks = treehouse_base_area / 5

# TO-DO: REPLACE THIS WITH A COMMENT DESCRIBING WHAT THE BELOW LINE OF CODE IS DOING
total_planks = treehouse_base_planks + treehouse_ladder_planks

# Display program output to user
print(f"You'll need {total_planks} to build a treehouse that has a base of {treehouse_width} feet by {treehouse_length} feet.")