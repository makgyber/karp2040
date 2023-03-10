import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP12,
        board.GP13,
        board.GP29,
        board.GP28,
        board.GP27,
        board.GP5,
        board.GP4,
        board.GP8,
        board.GP9,
        board.GP10,
    )
    row_pins = (
        board.GP7,
        board.GP26,
        board.GP15,
        board.GP14,
    )
    diode_orientation = DiodeOrientation.ROW2COL
