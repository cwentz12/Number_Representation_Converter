"""
This program is a number representation converter. In a main menu loop,
the user has the option to convert a number in base 10 (decimal) to the
common binary and hexadecimal representations, to see the number converted to
all bases 2-36, to convert a number in another base to decimal, to convert
a number in any base to any other base, or to convert a number in any base 2-36 to
all other bases. At any time in the main menu, the user can enter 'q' to quit the program.
The program uses input validation functions that show the user a list of valid symbols to
create a number in a given base.

Author: Chris Wentz
Date Created: April 20, 2023 [Last Modified: April 20, 2023]
"""


def print_menu():
    """ Prints the menu of options including the option to quit"""
    print("-" * 56)
    print("NUMBER REPRESENTATION CONVERTER: \n")
    print("1) Convert a number in decimal to binary and hexadecimal")
    print("2) Convert a number in decimal to all bases 2-36")
    print("3) Convert a number in another base to decimal")
    print("4) Convert a number in any base to any other base")
    print("5) Convert a number in any base to all other bases 2-36")
    print("Enter a command ('q' to quit): ")


def collect_valid_user_integer():
    """ Input validation that ensures a valid non-negative integer is produced and returned"""
    user_number = -1
    while user_number < 0:
        try:
            user_number = int(input("Enter a non-negative integer (0, 1, 2, ...): "))
            if user_number < 0:
                raise ValueError
        except ValueError:
            print("Error: That is not a non-negative integer.")
    return user_number


def collect_valid_alphanumeric(user_base):
    """
    This provides input validation to ensure a user enters an appropriate
    string of digits and letters for a given base. For example, for a
    base of 2, the user will be prompted to enter a string using 0's and 1's.
    For base 16, the user will be told they can use 0-9 and A-F. The final valid
    string is returned.
    """

    base_36_character_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6",
                              7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C",
                              13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I",
                              19: "J", 20: "K", 21: "L", 22: "M", 23: "N", 24: "O",
                              25: "P", 26: "Q", 27: "R", 28: "S", 29: "T", 30: "U",
                              31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z"}

    # Returns a string from a list splice of acceptable alphanumeric values for a given base
    valid_characters = ''.join(list(base_36_character_dict.values())[:user_base])

    while True:
        error_found = False
        user_number = input(f"Enter an alphanumeric number using {valid_characters}: ").upper()
        if len(user_number) == 0:
            continue
        for character in user_number:
            if character not in valid_characters:
                print(f"The '{character}' symbol is not valid.\n")
                error_found = True
                break
        if not error_found:
            return user_number


def collect_valid_user_base():
    """ Ensures a user inputted base is an integer between 2 and 36 and returns it"""
    user_base = 0
    while (user_base < 2) or (user_base > 36):
        try:
            user_base = int(input("Enter a valid integer base (2-36): "))
            if (user_base < 2) or (user_base > 36):
                raise ValueError
        except ValueError:
            print("Error: That is not a valid base.")
    return user_base


def base_n_to_decimal(number, current_base):
    """
    This converts a number in a given base into its base 10 decimal representation.
    It iterates through a reversed string of the number to find the cumulative sum of
    each character's integer value times the current base to the current power. The final
    sum is the base 10 decimal representation. For example, 1010 in base 2 (binary) becomes
    (0 * 2^0) + (1 * 2^1) + (0 * 2^2) + (1 * 2^3) = 0 + 2 + 0 + 8 = 10 in base 10 (decimal).
    """

    decimal_num = 0  # Used to collect the final sum
    current_power = 0

    # Reverses the string and capitalizes any letters.
    # It iterates through the string, incrementing the power by one each time
    # to find and return the total sum. The total sum is the base 10 decimal representation.
    for digit in reversed(number.upper()):
        if digit.isdigit():
            decimal_num += int(digit) * (current_base ** current_power)
        else:
            # Converts ASCII characters to their decimal integer equivalent
            # e.g. A is 65, 65 - 55 = 10, the equivalent value of A in decimal
            decimal_num += (ord(digit) - 55) * (current_base ** current_power)
        current_power += 1
    return decimal_num


def decimal_to_base_n(number, target_base):
    """
    This converts a number from its base 10 decimal representation to another
    base. It uses a dictionary to map integer values to their corresponding
    alphanumeric equivalents. The loop builds numbers from right to left by using
    the remainder of the number divided by the target base to select the corresponding
    character in the dictionary.
    """

    base_36_character_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6",
                              7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C",
                              13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I",
                              19: "J", 20: "K", 21: "L", 22: "M", 23: "N", 24: "O",
                              25: "P", 26: "Q", 27: "R", 28: "S", 29: "T", 30: "U",
                              31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z"}
    if number == 0:
        return "0"
    target_base_number = ""
    while number > 0:
        remainder = number % target_base
        target_base_number = base_36_character_dict[remainder] + target_base_number
        number //= target_base
    return target_base_number


def main():
    """
    The main method runs the main menu loop and calls functions to serve user requests.
    The program is terminated when the user enters 'q' to quit.
    """
    user_command = ""
    while user_command != "q":
        print_menu()
        user_command = input()
        match user_command:
            case "1":  # Convert a number in decimal to binary and hexadecimal
                user_number = collect_valid_user_integer()
                print(f"\n{user_number} in Decimal is: ")
                print(f"Binary (Base 2): {decimal_to_base_n(user_number, 2)}")
                print(f"Hexadecimal (Base 16): {decimal_to_base_n(user_number, 16)}\n")

            case "2":  # Converts decimal to all other bases
                user_number = collect_valid_user_integer()
                print(f"{user_number} in Base 10: ")
                print("-" * 56)
                for i in range(2, 37):  # Goes from base 2 to base 36
                    print(f"Base {i}: {decimal_to_base_n(user_number, i)}")

            case "3":  # Converts another base to decimal
                user_base = collect_valid_user_base()
                user_number = collect_valid_alphanumeric(user_base)
                print(f"{user_number} in Base {user_base} is: ")
                print(f"Decimal (Base 10): {base_n_to_decimal(user_number, user_base)}\n")

            case "4":  # Converts any base to another base
                print("Enter a number and base to convert from: ")
                user_base1 = collect_valid_user_base()
                user_number1 = collect_valid_alphanumeric(user_base1)
                print("Enter the base to convert to: ")
                user_base2 = collect_valid_user_base()
                converted_num = decimal_to_base_n(base_n_to_decimal(user_number1, user_base1), user_base2)
                print(f"{user_number1} in Base {user_base1} is: ")
                print(f"Base {user_base2}: {converted_num}\n")

            case "5":  # Converts any base to all other bases
                user_base = collect_valid_user_base()
                user_number = collect_valid_alphanumeric(user_base)
                print(f"{user_number} in Base {user_base}: ")
                print("-" * 56)
                for i in range(2, 37):
                    converted_num = decimal_to_base_n(base_n_to_decimal(user_number, user_base), i)
                    print(f"Base {i}: {converted_num}")

            case "q":  # Quits the program
                break

            case other:  # Handles invalid input
                print("Invalid command.")
                print_menu()
                user_command = input()

    print("*** Goodbye! ***")  # Final program message when user quits


if __name__ == '__main__':
    main()
