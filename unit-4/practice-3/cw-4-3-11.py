"""
animal_type: Christine Wei
Date: April 21, 2023,
Description: Pet class
"""


class Pet(object):
    """
    Parameters: name, animal_type, age
    Instance variables: name, animal_type, age
    Accessor methods: get_name(), get_animal_type(), get_age()
    Mutator methods: set_name(), set_animal_type(), set_age()
    """
    def __init__(self, name, animal_type, age):
        """
        Initializes object's data attributes
        """
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_name(self):
        """
        Accessor method
        Accepts no parameters
        Returns animal's name
        """
        return self.__name

    def get_animal_type(self):
        """
        Accessor method
        Accepts no parameters
        Returns animal type
        """
        return self.__animal_type

    def get_age(self):
        """
        Accessor method
        Accepts no parameters
        Returns animal's age
        """
        return self.__age

    def set_name(self, new_name):
        """
        Mutator method
        Accepts new name as parameter
        Changes animal name to its new name if new name is valid. If invalid, new name is Unknown
        Returns nothing
        """
        if new_name != "":
            self.__name = new_name
        else:
            self.__name = "Unknown"

    def set_animal_type(self, new_animal_type):
        """
        Mutator method
        Accepts new animal type as parameter
        Changes animal type to its new type if new type is valid. If invalid, type is changed to Dog
        Returns nothing
        """
        animal_types = ["Dog", "Cat", "Bird"]

        if new_animal_type in animal_types:
            self.__animal_type = new_animal_type
        else:
            self.__animal_type = "Dog"

    def set_age(self, new_age):
        """
        Mutator method
        Accepts new animal age as parameter
        Changes animal age to its new age if new age is valid. If age is negative, age is changed to Dog
        Returns nothing
        """
        if new_age >= 1:
            self.__age = new_age
        else:
            self.__age = 1

    def __str__(self):
        """
        Returns the pets name, age, and animal type in a summary sentence
        """
        return f"{self.__name} is a {self.__age} year old {self.__animal_type}"


def main():
    # Create an instance of the pet object
    pet = Pet("Fluffy", "Dog", 7)

    # Displays info before pet has changed
    print(f"""
    name: {pet.get_name()}
    animal_type: {pet.get_animal_type()}
    age: {pet.get_age()}""")

    print("\n", pet, "\n")

    # Changes pet info
    print("You have found that Fluffy is not who they seem to be, Someone has misinputed their data!"
          "Please change their name, animal type, and age", "\n")

    pet.set_name(input("Correct name: "))
    pet.set_animal_type(input("Correct animal type: "))
    pet.set_age(int(input("Correct age: ")))

    # Displays info after pet has changed
    print(f"""
    name: {pet.get_name()}
    animal_type: {pet.get_animal_type()}
    age: {pet.get_age()}""")

    print("\n", pet)


main()
