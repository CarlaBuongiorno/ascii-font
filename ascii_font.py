def ascii_font(letter):
    with open('ascii_font.txt') as ascii:
        font_file = ascii.readlines()
        font_file = [line.strip('\n') for line in font_file]
        result = []
        [result.append((item, [])) if item.isalpha() else result[-1][1].append(item) for item in font_file]
        for l, font in result:
            if l == letter:
                return font
        return result

#  starting on line 2
#  make a list of each letter
#  so add all the lines under each letter and until the empty line into a list
#  can be a list of tuples with the letter as the first index
#  and the list as the second index