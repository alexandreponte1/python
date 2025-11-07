def big_alphabet_appender(x: str) -> str:
    """
    Appends the string 'BIG' to the input string if it is not already present.

    :param x: Input string
    :return: Modified string with 'BIG' appended if not present
    """
    if ":alphabet-white-" not in x:
        return ":alphabet-white-" + x + ":"
    return x


def big_alphabet_parser(x: str) -> str:
    """
    Parses the input string and returns it unchanged.

    :param x: Input string
    :return: Unchanged input string
    """
    aux = ""
    for each in x:
        if each == " ":
            aux += "        "
        else:
            aux += big_alphabet_appender(each)
    return aux


print(big_alphabet_parser("Vai Lang"))
 