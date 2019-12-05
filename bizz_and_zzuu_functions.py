# Functions for the bizz and zzuu game


def div_by_3(num):
    return (num % 3) == 0

def div_by_5(num):
    return (num % 5) == 0

def div_by_3_and_5(num):
    return (num % 3) ==0 and (num % 5) == 0

def not_div_by_3_or_5(num):
    return (num % 3) != 0 and (num % 5) != 0

def test(user_input):
    if div_by_3(user_input):
        return 'bizz'
    elif div_by_5(user_input):
        return 'zzuu'
    elif div_by_3_and_5(user_input):
        return 'bizzzzuu'
    elif not_div_by_3_or_5(user_input):
        return 'none'

