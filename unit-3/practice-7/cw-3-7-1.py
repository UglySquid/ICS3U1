"""
Author: Christine Wei
Date: March 31, 2023,
Description: Opens file and keeps track of how many instances of each word
"""

with open("textfile.txt") as f:
    text_string = ""

    for line in f:
        text_string += f.readline().strip()
    f.close()

text_string = text_string.replace(".", "").replace(")", "").replace("(", "").replace(",", "")

d = {}

for x in range(len(text_string.split())):
    word = text_string.split()[x]
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

new_file = open("report.txt", "a")

for x in range(0, len(list(d))):
    word_key = list(d)[x]
    new_file.write(f"Word: {word_key}; Word count: {d[word_key]} \n")

new_file.close()
