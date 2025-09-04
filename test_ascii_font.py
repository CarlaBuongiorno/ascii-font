from ascii_font import ascii_font


def test_ascii_font():
    assert ascii_font


def test_print_letter():
    assert ascii_font('A') == [
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