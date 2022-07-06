import os
import gitit
import shutil
from dotenv import dotenv_values

TREE = dotenv_values('.tree')


# DO NOT TOUCH ANYTHING ABOVE THIS LINE!!


def area_of_rectangle(width: int, length: int) -> int:
    # TO-DO: CALCULATE AREA OF A RECTANGLE GIVEN WIDTH AND LENGTH
    return area

def area_of_square(): # TO-DO: DETERMINE FUNCTION INPUT & OUTPUT (USE TYPE ANNOTATIONS)
    area = width * 2
    # TO-DO: IMPLEMENT APPROPRIATE RETURN STATEMENT

def area_of_circle(radius: int) -> float:
    # TO-DO: CALCULATE THE AREA OF A CIRCLE
    # YOU MAY NEED TO LOOK UP THE EQUATION FOR THE AREA OF A CIRCLE
    # (APPROXIMATE PI TO 3.14)
    # YOU MAY ALSO NEED TO LOOK UP HOW TO USE EXPONENTS IN PYTHON
    return area


def main():

    # DO NOT TOUCH BELOW MEASUREMENTS!
    north_to_south_length = 18
    west_to_east_width = 24
    wall_height = 7
    window_width = 2
    window_height = 3
    tree_radius = 4
    entry_hole_width = 5
    # DO NOT TOUCH ABOVE MEASUREMENTS!


    # TO-DO: USING SOME COMBINATION OF THE THREE FUNCTIONS area_of_rectangle(), area_of_square(), area_of_circle()...
    # ...DETERMINE THE AREA OF EACH OF THE FOUR WALLS AND THE FLOOR...
    # ...THEN STORE THE TOTAL AREA OF ALL FIVE SURFACES IN THE BELOW VARIABLE total_treehouse_area

    total_treehouse_area = 


    # DO NOT TOUCH ANYTHING BELOW THIS LINE!!


    # NEED TO IMPLEMENT SCRIPT STEPS (COMPARE SOLUTION, CONVERT BIG-OAK-TREE TO TREEHOUSE)
    print()
    print(f"Looks like {total_treehouse_area} square feet of wood is needed to make the treehouse...")
    print()
    if total_treehouse_area == float(TREE["sqft"]):
        if os.path.exists("../treehouse/message-carved-in-tree.md"):
            print("...but you've already got a spiffy treehouse. Not much else to see here.")
            print()
        else:
            print(f"...and sure enough, the autonomous robot builder R2B2 whirs to life!")
            print(f"Success!")
            print()
            shutil.rmtree("../big-oak-tree")
            os.mkdir("../treehouse")
            gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-2-additions/treehouse/message-carved-in-tree.md", "../treehouse/message-carved-in-tree.md")
            print("R2B2 seems to move a *lot* faster than that vacuum from earlier.")
            print("Before you know it, there's a treehouse in your backyard!")
            print()
            print("You oughta go check it out!")
            print()
    else:
        print(f"...but the autonomous robot builder R2B2 doesn't appear to budge.")
        print()
        print("Maybe you got something wrong along the way?")
        print("Best to recheck the program...")
        print()
    


if __name__ == "__main__":
    main()