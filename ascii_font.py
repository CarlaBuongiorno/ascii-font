def convert_to_ascii(ascii_font, text):
        for l, font in ascii_font:
            if l == text:
                return font
        return ascii_font

#  starting on line 2
#  make a list of each letter
#  so add all the lines under each letter and until the empty line into a list
#  can be a list of tuples with the letter as the first index
#  and the list as the second index