import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys


keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

modtap = ModTap()
keyboard.modules.append(modtap)

NONE = KC.NO
COLEMAK = KC.DF(0)
NUM = KC.MO(1)
NAV = KC.MO(2)
ADJUST = KC.DF(3)

UNDO = KC.LGUI(KC.Z)
COPY = KC.LGUI(KC.C)
PASTE = KC.LGUI(KC.V)
CUT = KC.LGUI(KC.X)
SAVE = KC.LGUI(KC.S)
ALL = KC.LGUI(KC.A)

CLSFT = KC.MT(KC.C, KC.LSFT, prefer_hold=True,
              tap_interrupted=False, tap_time=3000)

ZLCTL = KC.MT(KC.Z, KC.LCTRL, prefer_hold=True,
              tap_interrupted=False, tap_time=3000)

XLALT = KC.MT(KC.X, KC.LALT, prefer_hold=True,
              tap_interrupted=False, tap_time=3000)

DOTALT = KC.MT(KC.DOT, KC.LALT, prefer_hold=True,
               tap_interrupted=False, tap_time=3000)

COMMAGUI = KC.MT(KC.COMM, KC.LGUI, prefer_hold=True,
                 tap_interrupted=False, tap_time=3000)

ENTERCTL = KC.MT(KC.ENTER, KC.LCTRL, prefer_hold=True,
                 tap_interrupted=False, tap_time=3000)

SPCSFT = KC.MT(KC.SPACE, KC.LSFT, prefer_hold=True,
               tap_interrupted=False, tap_time=3000)

ENTGUI = KC.MT(KC.ENTER, KC.LGUI, prefer_hold=False,
               tap_interrupted=False, tap_time=150)

NUMBSPC = KC.LT(1, KC.BSPC, prefer_hold=True,
                tap_interrupted=False, tap_time=250)
NAVSPC = KC.LT(2, KC.SPC, prefer_hold=True,
               tap_interrupted=False, tap_time=250)

JON = send_string('jon99')
ARROW = send_string('->')
DARROW = send_string('=>')
THE = send_string('the')
YOU = send_string('you')
OF_S = send_string('of')
ING = send_string('ing')
AND_S = send_string('and')

keyboard.keymap = [
    [  # COLEMAK
        KC.Q,  KC.W,  KC.F,     KC.P,    KC.B,                          KC.J,    KC.L,     KC.U,    KC.Y,   KC.SCLN,
        KC.A, KC.R,  KC.S,     KC.T,    KC.G,                           KC.M,    KC.N,     KC.E,    KC.I,   KC.O,
        ZLCTL,  XLALT,  CLSFT,     KC.D,    KC.V,                       KC.K,    KC.H,     COMMAGUI, DOTALT, ENTERCTL,
        NAVSPC, ENTGUI,  NONE, NONE, NONE, NONE, NONE, NONE,    SPCSFT,   NUMBSPC,
    ],
    [  # NUM
        KC.EXLM,  KC.AT,  KC.HASH,     KC.DLR,    KC.PERC,          KC.CIRC,    KC.AMPR,     KC.ASTR,    KC.LPRN,   KC.RPRN,
        KC.N1,  KC.N2,  KC.N3,     KC.N4,    KC.N5,                 KC.N6,    KC.N7,     KC.N8,    KC.N9,   KC.N0,
        KC.MUTE,  KC.VOLU, KC.VOLD,     ING,   ADJUST,              KC.LABK,   KC.RABK,   KC.TILDE,   KC.SLSH,   KC.QUES,
        NAVSPC, ENTGUI,  NONE, NONE, NONE, NONE, NONE, NONE,    SPCSFT,   NUMBSPC,

    ],
    [  # NAV
       KC.ESC,    KC.DEL,   KC.UP,  KC.BSPC, YOU,        KC.PIPE, KC.GRV, KC.UNDS,  KC.PLUS,  KC.DQUO,
        KC.TAB,   KC.LEFT,  KC.DOWN,  KC.RGHT, ARROW,                  KC.LCBR, KC.RCBR,  KC.MINS, KC.EQL, KC.QUOT,
        AND_S,  OF_S, THE,    JON, DARROW,                    KC.LBRC,  KC.RBRC, KC.BSLS, KC.BRID, KC.BRIU,
        NAVSPC, ENTGUI,  NONE, NONE, NONE, NONE, NONE, NONE,    SPCSFT,   NUMBSPC,

    ],
    [  # ADJUST
        KC.TRNS,  KC.TRNS,  KC.MS_UP,     KC.TRNS,    KC.TRNS,   KC.F1,  KC.F2,  KC.F3,     KC.F4,    KC.F5,
        KC.MW_UP,  KC.MS_LT,  KC.MS_DOWN,   KC.MS_RT,    KC.TRNS,   KC.F6,    KC.F7,     KC.F8,    KC.F9,   KC.F10,
        KC.MW_DN,  KC.MB_LMB,  KC.MB_MMB,     KC.MB_RMB,   COLEMAK,    KC.F11,  KC.F12,  KC.TRNS,     KC.TRNS,   KC.TRNS,
        NAVSPC, ENTGUI,                     NONE, NONE, NONE, NONE, NONE, NONE,         SPCSFT,   NUMBSPC,

    ]
]

if __name__ == '__main__':
    keyboard.go()
