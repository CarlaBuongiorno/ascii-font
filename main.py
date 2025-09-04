'''
Write a program to print ASCII Font versions of any text you give it. i.e.:

> python ascii-font.py A word
  *       * * *  ***  ***   ***
 * *      * * * *   * *  *  *  *
*   *      * *  *   * *  *  *  *
*****      * *  *   * ****  *  *
*   *      * *   ***  *   * *** 

Be as creative as you like! Don't use any external libraries or APIs.'''

from ascii_font import ascii_font


def main():
    print_ascii = ascii_font('A')
    print(print_ascii)
    # for char in print_ascii:
    #     print(char)


if __name__ == '__main__':
    main()