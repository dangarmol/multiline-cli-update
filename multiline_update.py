#!/usr/bin/env python3

import time


def multiline_update(lines: list) -> None:
    """
    Updates the last printed lines with the contents provided as a list of strings.
    You may wanna use `print("\\n"*(len(lines)-1))` before calling this function,
    for the first time, since it will overwrite whatever was in the console otherwise.

    Args:
       - `lines: list[str]` - List of lines to print. The lines cannot contain any `\\n` characters.
        One item = One line.
    """

    DISP = len(lines)
    UP = f"\x1B[{DISP}A"
    CLR = "\x1B[0K"
    printable_list = [UP, *[f"{line}{CLR}\n" for line in lines]]
    printable_list[-1] = printable_list[-1][:-1]  # Remove "\n" from last line.
    print("".join(printable_list))


# Or if you prefer it as a sick one-liner...
sick_multiline_update = lambda x:print("".join([f"\x1B[{len(x)}A",*["%s%s"%(f"{l}\x1B[0K","\n"if i!=(len(x)-1)else"")for i,l in enumerate(x)]]))
# ...there's no particular advantage to using this, just did it for fun.


# Usage
print("Function mode...")
print("\n"*3)  # Print 3 endlines because there will be 4 lines.
multiline_update(["hey 1", "hey 2", "hey 3", "hey 4"])
time.sleep(1)
multiline_update(["what's 1", "what's 2", "what's 3", "what's 4"])
time.sleep(1)
multiline_update(["up 1", "up 2", "up 3", "up 4"])
time.sleep(1)

print("Lambda mode...")
print("\n"*3)  # Print 3 endlines because there will be 4 lines.
sick_multiline_update(["hey 1", "hey 2", "hey 3", "hey 4"])
time.sleep(1)
sick_multiline_update(["what's 1", "what's 2", "what's 3", "what's 4"])
time.sleep(1)
sick_multiline_update(["up 1", "up 2", "up 3", "up 4"])
time.sleep(1)
