# Functions for the bizz and zzuu game


def div_by_3(num):
    if (num % 3) == 0:
        return 'bizz'

def div_by_5(num):
    if (num % 5) == 0:
        return 'zzuu'

def div_by_3_and_5(num):
    if (num % 3) ==0 and (num % 5) == 0:
        return 'bizzzzuu'

def not_div_by_3_or_5(num):
    if(num % 3) != 0 and (num % 5) != 0:
        return 'none'
