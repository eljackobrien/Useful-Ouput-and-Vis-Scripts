# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:54:20 2023

@author: eljac
"""

# =============================================================================
# A print function which uses ANSI escape codes (specifically the SGR = Select Graphic
# Rendition) parameters, to print formatted text to the console
# RGB colours for foreground and background as well as a couple of format strings are available
# See https://en.wikipedia.org/wiki/ANSI_escape_code for a full list of codes
# =============================================================================


fmt_dict = {"italic":3, "underlined":4}


def print_clr(obj='', fore_clr=(255,255,255), back_clr=(0,0,0), fmt:str=None, end='\n'):
    for clr_tuple in [fore_clr, back_clr]:
        if sum([0 > clr > 255 for clr in clr_tuple]):
            raise Exception("Ensure colour given is a 3-tuple or list of numbers N, where 0 < N < 255")

    if fmt in fmt_dict.keys(): fmt_code = f"\033[{fmt_dict[fmt]};m"
    else: fmt_code = "\033[2;m"

    fore_clr_code = f"\033[38;2;{fore_clr[0]};{fore_clr[1]};{fore_clr[2]};m"
    back_clr_code = f"\033[48;2;{back_clr[0]};{back_clr[1]};{back_clr[2]};m"

    print(f"{fore_clr_code}{back_clr_code}{fmt_code}{obj}\033[0;0m", end=end)



# Do some tests
if __name__ == "__main__":
    for i in range(25):
        print()
        for j in range(3):
            print_clr(f"TEST - {i,j}", fore_clr=(10*i,10*i,0), back_clr=(0,50+50*j,50+50*j), end='\t')

    print_clr()
    print_clr("TEST", fmt='italic')
    print_clr("TEST", fmt='underlined')
    print_clr("TEST", fmt='not a valid format')