'''
Author: Alexandr Iapara
Description: This program defines a function that reverses a string.
'''

import string


def reverse(string):
    """Return the reversed version of the input string.

    This function iterates through each character in the input string and
    constructs a new string by prepending each character, effectively reversing
    the original string.

    Args:
        string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    str = ""
    for i in string:
        str = i + str
    return str
  
def main():
    """Main function to demonstrate string reversal."""

    print("\033[32m" + "=" * 39 + "\033[0m")
    print("\033[32mWelcome to the String Reversal Program!\033[0m")
    while True:
        try:
            user_input = input("\033[33m\nEnter a string to reverse (or type 'exit' to quit): \033[0m")
            
            if user_input.lower() == 'exit':
                print("\033[33mExiting the program.\n\033[0m")
                break

            reversed_string = reverse(user_input)
            print(f"\033[33m\nOriginal:\033[0m {user_input}")
            print(f"\033[33mReversed:\033[0m {reversed_string}\n")
            return

        except KeyboardInterrupt:
            print("\033[33m\nProgram interrupted. Exiting.\033[0m\n")
            break
        except Exception as e:
            print(f"\033[31mAn error occurred: {e}\033[0m")

if __name__ == "__main__":
    main()