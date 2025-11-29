#!/usr/bin/python3
for char_code in range(97, 123):
    if char_code != 101 and char_code != 113:  # 101 is 'e', 113 is 'q'
        print("{}".format(chr(char_code)), end="")
