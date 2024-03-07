"""
animal_type: Christine Wei
Date: April 24, 2023,
Description: Monsters class
"""


class Monster(object):
    def __init__(self, monster_name):
        self.set_name(monster_name)

    def set_name(self, monster_name):
        """
        Description: This function initializes the data attributes of the monster object
        Parameter: String
        Output/Action: Initializes the data attributes
        """
        if monster_name:
            self.__name = monster_name
        else:
            self.__name = "Unknown"

    def get_name(self):
        """
        Description: This function returns the monster's name.
        Parameter: None
        Output: String
        """
        return self.__name

    def speak(self):
        """
        Description: This function displays a statement that shows the monster's name
        Parameter: String
        Output/Action: Displays a string that tells user the name
        """
        print("I am a monster named " + self.__name + "." )


class Skeleton(Monster):
    def __init__(self, hungry, monster_name):
        """
        Description: This function initializes the data attributes of the skeleton object
        Parameter: Boolean
        Output/Action: Initializes the data attributes
        """
        super().__init__(monster_name)
        self.__hungry = hungry

    def set_hunger(self, hungry):
        """
        Description: This function allows the user to set the skeleton's hungriness to hungry or not hungry
        Parameter: Boolean
        Output/Action : Changes the data attribute self.__hungry
        """
        self.__hungry = hungry

    def get_hunger(self):
        """
        Description: This function returns a string statement that describes if they are hungry or not.
        Parameter: None
        Output: String
        """
        if self.__hungry is True:
            return "hungry"
        else:
            return "not hungry"


def main():
    """
    Main line logic to display the uses of the Skeleton and the Monster classes
    """
    my_skeleton = Skeleton(True, "Best-friend")

    print("I have not fed my skeleton.")
    print(f"My skeleton is currently {my_skeleton.get_hunger()}")

    print("I have fed my skeleton.")
    my_skeleton.set_hunger(False)
    print(f"My skeleton is currently {my_skeleton.get_hunger()}")


main()
