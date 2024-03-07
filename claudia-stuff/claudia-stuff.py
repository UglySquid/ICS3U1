
class Pets:
    # where the attributes are
    def __int__(self, name, animal_type, age):
        self.__animal_type = animal_type
        self.__age = age
        self.__name = name

    def get_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


def main():
    pet = Pets()
    print(pet.get_name(), pet.get_age(), pet.get_type())


main()
