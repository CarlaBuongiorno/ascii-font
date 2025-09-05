def ascii_file_handling(): # returns list of tuples containing a string and list of strings [('A', ['      ______', '     |_    _|'])]
    with open('ascii_font.txt') as font_file:
        ascii_text = font_file.readlines()
        ascii_text = [line.strip('\n') for line in ascii_text]
        ascii_data = []
        [ascii_data.append((item, [])) if item.isalpha() else ascii_data[-1][1].append(item) for item in ascii_text]
        return ascii_data