"""Ascii value list"""

"""
Here are the **ASCII values** for the characters in the ranges you asked for:

### Lowercase Letters (`a-z`):
| Character | ASCII Value |
|-----------|-------------|
| a         | 97          |
| b         | 98          |
| c         | 99          |
| d         | 100         |
| e         | 101         |
| f         | 102         |
| g         | 103         |
| h         | 104         |
| i         | 105         |
| j         | 106         |
| k         | 107         |
| l         | 108         |
| m         | 109         |
| n         | 110         |
| o         | 111         |
| p         | 112         |
| q         | 113         |
| r         | 114         |
| s         | 115         |
| t         | 116         |
| u         | 117         |
| v         | 118         |
| w         | 119         |
| x         | 120         |
| y         | 121         |
| z         | 122         |

### Uppercase Letters (`A-Z`):
| Character | ASCII Value |
|-----------|-------------|
| A         | 65          |
| B         | 66          |
| C         | 67          |
| D         | 68          |
| E         | 69          |
| F         | 70          |
| G         | 71          |
| H         | 72          |
| I         | 73          |
| J         | 74          |
| K         | 75          |
| L         | 76          |
| M         | 77          |
| N         | 78          |
| O         | 79          |
| P         | 80          |
| Q         | 81          |
| R         | 82          |
| S         | 83          |
| T         | 84          |
| U         | 85          |
| V         | 86          |
| W         | 87          |
| X         | 88          |
| Y         | 89          |
| Z         | 90          |

### Digits (`0-9`):
| Character | ASCII Value |
|-----------|-------------|
| 0         | 48          |
| 1         | 49          |
| 2         | 50          |
| 3         | 51          |
| 4         | 52          |
| 5         | 53          |
| 6         | 54          |
| 7         | 55          |
| 8         | 56          |
| 9         | 57          |

### Special Characters:
Here are some common special characters and their ASCII values:

| Character  | ASCII Value |
|------------|-------------|
| ` `        | 32          |
| `!`        | 33          |
| `"`        | 34          |
| `#`        | 35          |
| `$`        | 36          |
| `%`        | 37          |
| `&`        | 38          |
| `'`        | 39          |
| `(`        | 40          |
| `)`        | 41          |
| `*`        | 42          |
| `+`        | 43          |
| `,`        | 44          |
| `-`        | 45          |
| `.`        | 46          |
| `/`        | 47          |
| `:`        | 58          |
| `;`        | 59          |
| `<`        | 60          |
| `=`        | 61          |
| `>`        | 62          |
| `?`        | 63          |
| `@`        | 64          |
| `[`        | 91          |
| `\`        | 92          |
| `]`        | 93          |
| `^`        | 94          |
| `_`        | 95          |
| ```        | 96          |
| `{`        | 123         |
| `|`        | 124         |
| `}`        | 125         |
| `~`        | 126         |

These are the most common ASCII characters in the ranges you asked for, from `a-z`, `A-Z`, `0-9`, and various special characters.
"""


def convert_char_to_ascii():
    char = 'A'
    ascii_value = ord(char)
    print(ascii_value)


def convert_ascii_to_char():
    ascii_value = 65
    char = chr(ascii_value)
    print(char)

def check_char_is_alpha_numeric():
    s = 'abc1_f,'
    for char in s:
        if char.isalnum():
            print(char)

if __name__ == '__main__':
    convert_ascii_to_char()
    convert_char_to_ascii()
    check_char_is_alpha_numeric()