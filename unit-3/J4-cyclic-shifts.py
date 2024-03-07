text = input()
string_shift = input()

# cyclic_shift = []
#
# start = 0
#
# for i in range(start, len(string_shift)):
#     temp = string_shift[0:i]
#     cyclic_shift.append(string_shift[i:(len(string_shift))] + temp + " ")
#     start += 1
#
# not_in = None
#
# for shift in cyclic_shift:
#     if shift in text:
#         not_in = False
#         print("yes")
#     else:
#         not_in = True
#
# if not_in:
#     print("no")

not_in = None

if not_in:
    print("no")

if text == string_shift:
    print("yes")
else:
    for i in range(0, len(string_shift)):
        string_shift = string_shift[i:-1]
        if string_shift == text:
            print("yes")
            not_in = False
        else:
            not_in = True
        print(string_shift)

if not_in:
    print("no")

