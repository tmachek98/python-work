#This function is a generator that will provide us a range of characters.
#These are based on Unicode points for the starting character and ending character 
#With an optional step value.

def char_range(start, stop, step=1):
    stop_modifier = 1
    start_code = ord(start)
    stop_code = ord(stop)

    if start_code > stop_code:
        step *= -1
        stop_modifier *= -1

    for value in range(start_code, stop_code + stop_modifier, step):
        yield chr(value)
        