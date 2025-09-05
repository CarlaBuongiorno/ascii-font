from ascii_file_handling import ascii_file_handling
from ascii_font import convert_to_ascii


def test_ascii_font():
    assert convert_to_ascii


def test_print_letter():
    ascii_font = ascii_file_handling()
    assert convert_to_ascii(ascii_font, 'A') == [
        '      ______',
        '     |_    _|',
        '      /    \\',
        '     /  /\\  \\',
        '    /  /__\\  \\', 
        '   /   ____   \\',
        ' _/   /_  _\\   \\_',
        '|_______||_______|',
        ''
    ]