#File Name: cupstoounces_NayleneRondon
#Date:2/22/17
#Programmer: Naylene Rondon
#Purpose: convert cups to ounces

def main():
    """Primary Function that calls other functions."""
    intro()
    Cup = Input()
    Ounce = convert(Cup)

    print("\n" + str(Cup) + " cups is equal to " + str(Ounce) + " ounces.")

def intro():
    """Introduction"""
    print("Welcome. Let's convert cups to ounces.")
    

def Input():
    """Takes user input and applies to cups"""
    cups = int(input("How many cups do you have? "))

    return cups


def convert(cups):
    """Multiples cup by eight to get ounces."""
    ounces = int(cups * 8)

    return ounces

main()
