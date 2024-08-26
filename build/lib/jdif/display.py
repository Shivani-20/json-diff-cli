import platform
import math
import os
import charade
from pyparsing import *
from termcolor import colored

# to get length of colored strings
def getActualLength(str):
    ESC = Literal('\x1b')
    integer = Word(nums)
    escapeSeq = Combine(ESC + '[' + Optional(delimitedList(integer,';')) + oneOf(list(alphas)))
    nonAnsiString = lambda s : Suppress(escapeSeq).transformString(s)
    unColorString = nonAnsiString(str)
    return len(unColorString)


# word-break purpose when line ends
def make_substrings(s, L):
    i = 0
    pieces = []
    color = findColor(s[0:10])
    j=L
    pieces.append(s[0:L])
    for i in range(j, len(s), L):
        pieces.append(colored(s[i:i+L],color))
    return pieces


# helper- to give the to strings whn they are broken while printing
def findColor(s):
    if s.startswith("\"\x1b[31m"):
        return "red"
    elif s.startswith("\"\x1b[32m"):
        return "green"
    return "white"


# Print lines side by side for colored text
def customFormat(token1,token2):
    rem_space=col_width-getActualLength(token1)
    line_fmt = ''
    token1 = token1 + (' ' * rem_space)
    line_fmt += ('{:<' + '}'
            + (' ' * math.floor((col_padding-len(delimiter))/2.))
            + colored(delimiter,"white")
            + (' ' * math.ceil((col_padding-len(delimiter))/2.))
            + '{:<' + '}')
    print(line_fmt.format(token1, token2))

    
def print_side_by_side(output1, output2):
    # Determine OS name to get terminal size
    if platform.system() == 'Windows':
        terminal_dimensions = os.get_terminal_size()
        rows, columns = terminal_dimensions.lines, terminal_dimensions.columns
    # Linux or Mac
    else:
        rows, columns = map(int, os.popen('stty size', 'r').read().split())
    # Split files into lines and strip off whitespace from each corner
    lines1 = output1.split('\n')
    lines2 = output2.split('\n')
    lines1=[i.strip() for i in lines1]
    lines2=[i.strip() for i in lines2]
    max_num_lines = max(len(lines1), len(lines2))
    global delimiter
    delimiter='|'
    global col_padding
    col_padding=2
    global col_width
    col_width = (columns - col_padding) // 2
    line_fmt = ''
    # Print lines side by side for normal text
    line_fmt += ('{:<' + str(col_width) + '}'
               + (' ' * math.floor((col_padding-len(delimiter))/2.))
               + colored(delimiter,"white")
               + (' ' * math.ceil((col_padding-len(delimiter))/2.))
               + '{:<' + str(col_width) + '}')

    for i in range(max_num_lines):
        # Get rows for this line for file 1.
        l1 = ''
        if i < len(lines1):
            l1 = lines1[i]
        row1 = make_substrings(l1, col_width)
        # Get rows for this line for file 2.
        l2 = ''
        if i < len(lines2):
            l2 = lines2[i]
        row2 = make_substrings(l2, col_width)
        max_num_rows = max(len(row1), len(row2))
        j = 0
        while j < max_num_rows:
            token1 = row1[j] if j < len(row1) else ''
            token2 = row2[j] if j < len(row2) else ''         
            x=charade.detect(token1.encode())
            y=charade.detect(token2.encode())
            if x["encoding"]=="ascii" and y["encoding"]==ascii:
                print(line_fmt.format(token1, token2))
            else:
                customFormat(token1, token2)
            j += 1