
def plant(flower_name: str, flower_color: str, flower_quantity: int) -> str:
    descriptive_flower_string = f"{flower_quantity} {flower_color} {flower_name}"
    return descriptive_flower_string
    
def main():
    original_flower_name = "balloon flowers"
    original_flower_color = "red"
    original_flower_quantity = 99
    original_flower_description = plant(original_flower_name, original_flower_color, original_flower_quantity)
    print()
    print(f"You see the previous tenant had planted {original_flower_description}.")
    print()
    print("They're lovely, but you think the flowerbed could use *more*.")
    print()

    # TO-DO: ASK USER FOR NAME OF FLOWER THEY'D LIKE TO PLANT, STORE RESPONSE

    # TO-DO: ASK USER FOR COLOR OF FLOWER TO PLANT, STORE RESPONSE

    # TO-DO: ASK USER FOR QUANTITY OF FLOWER TO PLANT, CONVERT TO AN INTEGER AND STORE RESPONSE

    # TO-DO: CALL plant() FUNCTION AND PASS ABOVE USER INPUTS; ORDER MATTERS--LOOK AT THE plant() FUNCTION SIGNATURE
    # BE SURE TO SAVE THE FUNCTION'S OUTPUT WITHIN THE VARIABLE flower_description

    print()
    print(f"Now the flowerbed also has {flower_description}. Lovely!")


if __name__ == "__main__":
    main()