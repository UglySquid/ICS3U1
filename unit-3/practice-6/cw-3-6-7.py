"""
Author: Christine Wei
Date: March 30, 2023,
Description: Counts the average number of words and the average number of characters per word
"""


def average_text(text):
    """
    Accepts file as argument
    Calculates average number of words per sentence, and the average number of characters per word.
    Returns the average number of words per sentence, and the average number of characters per word.
    """

    # open the file from where we want the content to be taken
    with open(text) as f:
        text_string = ""

        for line in f:
            text_string += f.readline().strip()
        f.close()

    # splits the text string into list where every list item is one sentence
    sentences = text_string.split(".")

    sum_words = 1
    sum_ch = 0

    # finds the sum of all the words and all the characters in the text file
    for i in range(0, len(sentences)):
        for ch in sentences[i]:
            if ch.isalpha():
                sum_ch += 1
            else:
                sum_words += 1

    # displays the average number of words per sentence, and the average number of characters per word.
    print(f"""average number of words per sentence: {sum_words/len(sentences)}
average number of characters per word: {sum_ch/sum_words}""")


average_text("textfile.txt")
