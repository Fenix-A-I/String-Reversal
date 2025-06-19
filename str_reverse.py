'''
Author: Alexandr Iapara
Description: This program defines a function that reverses a string.
'''

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
  
string = "This is a string to be reversed."
print(f"\nOriginal: {string}")
print(f"Reversed: {reverse(string)}\n")

