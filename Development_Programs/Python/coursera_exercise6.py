def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:     # <--- How many times is this line reached?
            matches = matches + 1
    return matches== (len(s) // 2)

