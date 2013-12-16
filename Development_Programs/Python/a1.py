def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time_2-time_1


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    return (time_2-time_1)/(60*60)


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    return ((hours*60*60+minutes*60+seconds)/(60*60))


def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """
    return hours % 24


def get_hours(time_1):
    """ (int) -> int

    Return the number of hours that have elapsed since midnight,
    as seen on a 24-hour clock, given a time in seconds (time_11).
    Not inclusive of minutes or seconds elapsed

    >>> get_hours(360)
    0
    >>> get_hours(3750)
    1
    >>> get_hours(36000)
    10
    >>> get_hours(39000)
    10
    >>> get_hours(93640)
    2
    >>> get_hours(-3655)
    22
    """
    return seconds//(60*60)%24


def get_minutes(time_1):
    """ (int) -> int

    Return the number of minutes that have elapsed since midnight,
    as seen on a 24-hour clock, given a time in seconds (time_1).
    Not inclusive of hours or seconds elapsed

    >>> get_minutes(360)
    6
    >>> get_minutes(3750)
    2
    >>> get_minutes(39000)
    50
    >>> get_minutes(93640)
    0
    >>> get_minutes(-3655)
    59
    """
    return seconds//(60)%60


def get_seconds(time_1):
    """ (int) -> int

    Return the number of seconds that have elapsed since midnight,
    as seen on a 24-hour clock, given a time in seconds (time_1).
    Not inclusive of hours or minutes elapsed

    >>> get_seconds(360)
    0
    >>> get_seconds(3750)
    30
    >>> get_seconds(39000)
    0
    >>> get_seconds(93640)
    0
    >>> get_seconds(-3655)
    5
    """
    return seconds%60


def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    Preconditions: -24<=utc_offset<=24 and 0<= time <=24

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    >>> time_to_utc(-3, 20.5)
    23.5
    >>> time_to_utc(-7, 20.5)
    3.5
    """
    return to_24_hour_clock(time-utc_offset)


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    >>> time_from_utc(-3, 20.5)
    17.5
    >>> time_from_utc(-7, 20.5)
    13.5
    """
    return to_24_hour_clock(24+time+utc_offset)

