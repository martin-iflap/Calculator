APP_SIZE = "400x700"
MAIN_ROWS = 7
MAIN_COLUMNS = 4

FONT = "Arial"
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 40


STYLING = {
    "gap": 0.5,
    "corner_radius": 0}

NUM_POSITION = {
    "." : {"col": 2, "row": 6, "span": 1},
    0  : {"col": 0, "row": 6, "span": 2},
    1  : {"col": 0, "row": 5, "span": 1},
    2  : {"col": 1, "row": 5, "span": 1},
    3  : {"col": 2, "row": 5, "span": 1},
    4  : {"col": 0, "row": 4, "span": 1},
    5  : {"col": 1, "row": 4, "span": 1},
    6  : {"col": 2, "row": 4, "span": 1},
    7  : {"col": 0, "row": 3, "span": 1},
    8  : {"col": 1, "row": 3, "span": 1},
    9  : {"col": 2, "row": 3, "span": 1}}

MATH_POSITIONS = {
    "/" : {"col": 3, "row": 2, "character": "/", "operator": "/"},
    "*" : {"col": 3, "row": 3, "character": "x", "operator": "*"},
    "-" : {"col": 3, "row": 4, "character": "-", "operator": "-"},
    "=" : {"col": 3, "row": 6, "character": "=", "operator": "="},
    "+" : {"col": 3, "row": 5, "character": "+", "operator": "+"}}

OPERATORS = {
    "clear": {"col": 0, "row": 2, "text": "AC"},
    "invert": {"col": 1, "row": 2, "text": "+-"},
    "percent": {"col": 2, "row": 2, "text": "%"}}