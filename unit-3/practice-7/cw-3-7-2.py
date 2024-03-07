"""
Author: Christine Wei
Date: March 31, 2023,
Description: Geek Translator
"""

geek = {"404": "clueless. From the web error message 404, meaning page not found.",
        "Googling": "searching the Internet for background information on a person.",
        "Keyboard Plaque": "the collection of debris found in computer keyboards.",
        "Link Rot": "the process by which web page links become obsolete.",
        "Percussive Maintenance": "the act of striking an electronic device to make it work.",
        "Uninstalled": "being fired. Especially popular during the dot-bomb era."}


def main():
    while True:
        choice = menu_input()

        if choice == 1:
            keep_going = look_up()
        elif choice == 2:
            keep_going = add_term()
        elif choice == 3:
            keep_going = redefine_term()
        elif choice == 4:
            keep_going = delete_term()
        else:
            break

        if not keep_going:
            continue
        else:
            break


def menu_input():
    while True:
        try:
            user_choice = int(input("""GEEK TRANSLATOR
1 - Look Up a Geek Term
2 - Add a Geek Term
3 - Redefine a Geek Term
4 - Delete a Geek Term
5 - Quit

"""))
            if 5 >= user_choice >= 1:
                return user_choice
            else:
                print("That number is not on the menu")
        except ValueError:
            print("That is not a number! Please try again.")
            continue


def look_up():
    term = input("Term to look up: ")

    try:
        print(f"Definition: {geek[term]}")
        return True
    except KeyError:
        print("Sorry, I don't know that term.")
        return False


def add_term():
    term = input("Term to add: ")

    if term not in geek:
        definition = input("Definition of term: ")
        geek[term] = definition
        print("The term has been added.")
        return True
    elif term in geek:
        "That term already exists! Try redefining it."
        return False


def redefine_term():
    term = input("Term to redefine: ")

    if term in geek:
        print(f"Term: {term} \nCurrent Definition:{geek[term]}")
        new_definition = input("New definition: ")
        geek[term] = new_definition
        print("Term has been redefined.")
        return True
    elif term not in geek:
        print("That term doesn't exists! Try adding it.")
        return False


def delete_term():
    term = input("Term to delete: ")

    remove_key = geek.pop(term, None)

    if remove_key is not None:
        print("Okay, I deleted the term.")
        return True
    else:
        print("Sorry, I don't know that term.")
        return False



main()
