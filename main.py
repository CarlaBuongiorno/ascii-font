'''
Write a program to print ASCII Font versions of any text you give it. i.e.:

> python ascii-font.py A word
  *       * * *  ***  ***   ***
 * *      * * * *   * *  *  *  *
*   *      * *  *   * *  *  *  *
*****      * *  *   * ****  *  *
*   *      * *   ***  *   * *** 

Be as creative as you like! Don't use any external libraries or APIs.'''

from ascii_file_handling import ascii_file_handling
from ascii_font import convert_to_ascii


def main():
    ascii_font = ascii_file_handling()
    text = 'A'
    print_ascii = convert_to_ascii(ascii_font, text)
    print(print_ascii)
    # for char in print_ascii:
    #     print(char)


if __name__ == '__main__':
    main()