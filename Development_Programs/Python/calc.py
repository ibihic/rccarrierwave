def square_return(num):
    return num**2

def square_print(num):
    print("ther square of num is", numm**2)

    
def convert_to_minutes(num_hours):
    '''(int)->int

    return the number of minutes there are in number hours.

    >>>convert_to_minutes(2)
    120
    '''

    result = num_hours * 60
    return result


def report_status(scheduled_time, estimated_time):
    '''(number, umber)-->str

    report_status(14.3,14.3)
    'on time'
    report_status(14.3,5.3)
    'early'
    report_status(7.3,14.3)
    'delayed'
    '''
    if scheduled_time==estimated_time:
        return "on time"
    elif scheduled_time>estimated_time:
        return 'early'
    else: 
        return 'delayed'

def is_even(num):
    '''(int) -> bool
    >>>is even(4)
    Trues
    >>> is_even(77)
    False
    '''
##    if num%2==0
##    return True
##else:
##    return False

    return num%2==0

len('')


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word_score = 0
    for c in word:
        word_score += score[c.lower()]
    return word_score


def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:     # <--- How many times is this line reached?
            matches = matches + 1
    return matches == (len(s) // 2)
