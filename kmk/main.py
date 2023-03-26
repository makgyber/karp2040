import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.handlers.sequences import send_string
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.extensions.LED import LED

led = LED(board.GP16)

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(led)
keyboard.modules.append(MouseKeys())

modtap = ModTap()
keyboard.modules.append(modtap)

combos = Combos()
keyboard.modules.append(combos)

# toggle all LEDs
LED_TOG_ALL = KC.LED_TOG()

NONE = KC.NO
QWERTY = KC.DF(1)
APTV3 = KC.DF(0)
NUM = KC.MO(2)
NAV = KC.MO(3)
ADJUST = KC.DF(4)

UNDO = KC.LGUI(KC.Z)
COPY = KC.LGUI(KC.C)
PASTE = KC.LGUI(KC.V)
CUT = KC.LGUI(KC.X)
SAVE = KC.LGUI(KC.S)
ALL = KC.LGUI(KC.A)

CLSFT = KC.MT(KC.C, KC.LSFT, prefer_hold=True,
              tap_interrupted=False, tap_time=175)

ZLCTL = KC.MT(KC.Z, KC.LCTRL, prefer_hold=True,
              tap_interrupted=False, tap_time=175)

XLALT = KC.MT(KC.X, KC.LALT, prefer_hold=True,
              tap_interrupted=False, tap_time=175)

CLALT = KC.MT(KC.C, KC.LALT, prefer_hold=True,
              tap_interrupted=False, tap_time=175)
XLCTL = KC.MT(KC.X, KC.LCTL, prefer_hold=True,
              tap_interrupted=False, tap_time=175)

DOTALT = KC.MT(KC.DOT, KC.LALT, prefer_hold=True,
               tap_interrupted=False, tap_time=175)

COMMAGUI = KC.MT(KC.COMM, KC.LGUI, prefer_hold=True,
                 tap_interrupted=False, tap_time=175)

ENTERCTL = KC.MT(KC.ENTER, KC.LCTRL, prefer_hold=True,
                 tap_interrupted=False, tap_time=175)

SPCSFT = KC.MT(KC.SPACE, KC.LSFT, prefer_hold=True,
               tap_interrupted=False, tap_time=175)
MSFT = KC.MT(KC.M, KC.LSFT, prefer_hold=True,
             tap_interrupted=False, tap_time=175)

ENTGUI = KC.MT(KC.ENTER, KC.LGUI, prefer_hold=False,
               tap_interrupted=False, tap_time=175)

NUMBSPC = KC.LT(2, KC.BSPC, prefer_hold=True,
                tap_interrupted=False, tap_time=175)
NAVSPC = KC.LT(3, KC.SPC, prefer_hold=True,
               tap_interrupted=False, tap_time=175)

JON = send_string('jon99')
ARROW = send_string('->')
DARROW = send_string('=>')
THE = send_string('the')
FOR_S = send_string('for')
OF_S = send_string('of')
ING = send_string('ing')
AND_S = send_string('and')
KO = send_string('ko')
NG = send_string('ng')

keyboard.keymap = [
    [  # APTv3
        KC.W,  KC.G, KC.D, KC.F,     KC.B,                             KC.Q,     KC.L, KC.U, KC.O, KC.Y,
        KC.R, KC.S, KC.T,  KC.H,    KC.K,                              KC.J,     KC.N,     KC.E,    KC.A,   KC.I,
        XLCTL,  CLALT,  MSFT,  KC.P,  KC.V,                              KC.Z,     KC.SCLN,  COMMAGUI, DOTALT, ENTERCTL,
        NAVSPC, ENTGUI,  NONE, NONE, NONE, NONE, NONE, NONE,    SPCSFT,   NUMBSPC,
    ],

    [  # QWERTY
        KC.Q,  KC.W, KC.E, KC.R,     KC.T,                             KC.Y,     KC.U, KC.I, KC.O, KC.P,
        KC.A, KC.S, KC.D,  KC.F,    KC.G,                         KC.H,     KC.J,     KC.K,    KC.L,   KC.SCLN,
        ZLCTL,  XLALT,  CLSFT,  KC.V,  KC.B,                       KC.N,      KC.M,    COMMAGUI, DOTALT, ENTERCTL,
        NAVSPC, ENTGUI,  NONE, NONE, NONE, NONE, NONE, NONE,    SPCSFT,   NUMBSPC,
    ],

    [  # NUM
        KC.EXLM,  KC.AT,  KC.HASH,     KC.DLR,    KC.PERC,          KC.CIRC,    KC.AMPR,     KC.ASTR,    KC.LPRN,   KC.RPRN,
        KC.N1,  KC.N2,  KC.N3,     KC.N4,    KC.N5,                 KC.N6,    KC.N7,     KC.N8,    KC.N9,   KC.N0,
        KC.MUTE,  KC.VOLU, KC.VOLD,     ING,   ADJUST,              KC.LABK,   KC.RABK,   KC.TILDE,   KC.SLSH,   KC.QUES,
        NAVSPC, ENTGUI,  NONE, NONE, NONE, NONE, NONE, NONE,      SPCSFT,   NUMBSPC,

    ],
    [  # NAV
        KC.ESC,    KC.DEL,   KC.UP,  KC.BSPC, FOR_S,        KC.PIPE, KC.GRV, KC.UNDS,  KC.PLUS,  KC.DQUO,
        KC.TAB,   KC.LEFT,  KC.DOWN,  KC.RGHT, ARROW,                  KC.LCBR, KC.RCBR,  KC.MINS, KC.EQL, KC.QUOT,
        AND_S,  OF_S, THE,    JON, DARROW,                    KC.LBRC,  KC.RBRC, KC.BSLS, KC.BRID, KC.BRIU,
        NAVSPC, ENTGUI,  NONE, NONE, NONE, NONE, NONE, NONE,    SPCSFT,   NUMBSPC,

    ],
    [  # ADJUST
        KC.TRNS,  KC.TRNS,  KC.MS_UP,     KC.TRNS,    KC.TRNS,   KC.F1,  KC.F2,  KC.F3,     KC.F4,    KC.F5,
        KC.MW_UP,  KC.MS_LT,  KC.MS_DOWN,   KC.MS_RT,    APTV3,   KC.F6,    KC.F7,     KC.F8,    KC.F9,   KC.F10,
        KC.MW_DN,  KC.MB_LMB,  KC.MB_MMB,     KC.MB_RMB,   QWERTY,    KC.F11,  KC.F12,  KC.TRNS,     KC.TRNS,   KC.TRNS,
        NAVSPC, ENTGUI,                     NONE, NONE, NONE, NONE, NONE, NONE,         SPCSFT,   NUMBSPC,

    ]
]

if __name__ == '__main__':
    keyboard.go()
