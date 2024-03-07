"""
Author: Christine Wei
Date: April 24, 2023,
Description: Person class
"""


class Person:
    def __init__(self, name, address, phone):
        """Initializes data attributes"""
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        """Returns person's name"""
        return self.__name

    def get_address(self):
        """Returns person's address"""
        return self.__address

    def get_phone(self):
        """Returns person's cell phone number"""
        return self.__phone

    def set_name(self, new_name):
        """Changes person's name"""
        self.__name = new_name

    def set_address(self, new_address):
        """Changes person's address"""
        self.__address = new_address

    def set_phone(self, new_phone):
        """Changes person's cell phone number"""
        self.__phone = new_phone


class Student(Person):
    def __init__(self, name, address, phone, student_id, cell_or_not):
        """Initializes data attributes"""
        super().__init__(name, address, phone)
        self.__student_id = student_id
        self.__have_cell = cell_or_not

    def get_student_id(self):
        """Returns student id"""
        return self.__student_id

    def get_cell_or_not(self):
        """Returns whether student has cell phone or not"""
        return self.__have_cell

    def set_student_id(self, new_id):
        """Changes student id"""
        self.__student_id = new_id

    def set_cell_or_not(self, have_cell):
        """Changes whether student has cell phone or not"""
        self.__have_cell = have_cell


def main():

    # Initializes instance of Student object
    christine = Student("Christine", "88 Hard Drive", None, 341044964, False)

    # Displays student's info (object's data attributes)
    print(f"Student info:")
    if christine.get_cell_or_not():
        number = christine.get_phone()
    else:
        number = "Student does not have cell phone"

    print(f"Name: {christine.get_name()}")
    print(f"Address: {christine.get_address()}")
    print(f"Cell phone number: {christine.get_phone()}")
    print(f"Student ID: {christine.get_student_id()}")

    # Change student info
    christine.set_name("Christine Wei")
    christine.set_student_id(123456789)
    christine.set_phone(123456789)
    christine.set_address("88 New Drive")
    christine.set_cell_or_not(True)

    # Displays new student info
    print(f"\nStudents {christine.get_name()} has moved")
    print(f"\nStudents {christine.get_name()}'s new info")

    if christine.get_cell_or_not():
        number = christine.get_phone()
    else:
        number = "Student does not have cell phone"

    print(f"Name: {christine.get_name()}")
    print(f"Address: {christine.get_address()}")
    print(f"Cell phone number: {christine.get_phone()}")
    print(f"Student ID: {christine.get_student_id()}")


main()
