#Week 6 Assignment CMIS 
def check_length(password):
    """Check if password is of valid length"""
    if len(password) < 6:
        return False, "Password length is too short"
    elif len(password) > 15:
        return False, "Password length is too long"
    else:
        return True, "Password length is valid"


def check_characters(password):
    """Check if password contains required number of characters/digits"""
    has_alpha = False
    has_digit = False

    for char in password:
        if char.isalpha():
            has_alpha = True
        elif char.isdigit():
            has_digit = True

        if has_alpha and has_digit:
            return True, "Password contains required number of characters/digits"

    return False, "Password must contain at least one alphabetic character and one digit"


def check_spaces(password):
    """Check if password contains spaces"""
    if " " in password:
        return False, "Password must not contain spaces"
    else:
        return True, "Password does not contain spaces"


# main function
def check_password(password):
    """Check if password meets all requirements"""
    length_check = check_length(password)
    if not length_check[0]:
        return length_check

    char_check = check_characters(password)
    if not char_check[0]:
        return char_check

    space_check = check_spaces(password)
    if not space_check[0]:
        return space_check

    return True, "Password is valid"


# prompt user for password
password = input("Enter password: ")

# check password validity
result = check_password(password)

# display results
print(result[1] if result[0] else result[1])