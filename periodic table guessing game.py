
"""To import random library of elements"""
import random

"""To define main() function"""
def main():
    """Start a periodic table game."""
    print("Guess the elements!")
    """To list down the elements in periodic table"""
    elements = [
        "hydrogen",
        "helium",
        "lithium",
        "beryllium",
        "boron",
        "carbon",
        "nitrogen",
        "oxygen",
        "fluorine",
        "neon"
        ]

    """To let the player choose random elements"""
    x = random.choice(elements)
    #print(x)
    guess = None

    """To execute a set of statements as long as a condition is true"""
    while x != guess:

        """To give multiple hints to the player"""
        guess = str(input("What element comes out in your mind? "))
        
        if   x == guess:
                print("You guessed {}. You're right! Great job!".format(guess))
        elif x == "hydrogen":   
                print("Try a non-toxic periodic table")
        elif x ==   "helium":
                print("Try a colourless.")
        elif x ==  "lithium":
                print("Try a mineral oil.")
        elif x =="beryllium":
                print("Try a hard metal.")
        elif x ==    "boron":
                print("Try an electricity.")
        elif x ==   "carbon":
                print("Try a soft.")    
        elif x == "nitrogen":
                print("Try a odourless gas.")
        elif x ==   "oxygen":
                print("Try a standard temperature.")
        elif x == "fluorine":
                print("Try a second-lighest noble gas.")
                break
        else:  
                print("You guessed {}. Nope,it's wrong. No worries,try again.!".format(guess))
"""To return to main() function"""
main()
