print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.modtap import ModTap
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.handlers.sequences import send_string
from kmk.modules.tapdance import TapDance


keyboard = KMKKeyboard()

keyboard.debug_enabled = True

keyboard.col_pins = (board.GP11,board.GP10,board.GP9,board.GP8,board.GP7,board.GP6,board.GP5,board.GP4,board.GP3,board.GP2)
keyboard.row_pins = (board.GP16,board.GP17,board.GP22,board.GP15)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


mediakeys = MediaKeys()

rgb = RGB(pixel_pin=board.GP21, num_pixels=9, animation_mode=AnimationModes.SWIRL, refresh_rate=60, animation_speed=4)

encoder_handler = EncoderHandler()

# Regular GPIO Encoder
encoder_handler.pins = ((board.GP18, board.GP19, board.GP14, False, 2),)

# You can optionally predefine combo keys as for your layout
Alt_tab_fwd = KC.LALT(simple_key_sequence((KC.MACRO_SLEEP_MS(50),KC.TAB))
Alt_tab_bwd = KC.LALT(KC.LSHIFT(simple_key_sequence((KC.MACRO_SLEEP_MS(50),KC.TAB)))

encoder_handler.map = [ ((KC.VOLD, KC.VOLU, KC.MUTE),), # Layer 1
                        ((Alt_tab_fwd, Alt_tab_bwd, KC.RGB_MODE_SWIRL),), # Layer 2
                        ((KC.A, KC.Z, KC.N1),), # NumPad not yet properly configured
                        ((KC.B, KC.Y, KC.N2),), # Gaming not yet properly configured
                      ]

layers = Layers()
layers.tap_time = 100

modtap = ModTap()
modtap.tap_time = 100

tapdance = TapDance()
tapdance.tap_time = 750

combos = Combos()

# Sequences

APPEND = simple_key_sequence((KC.TG(0), KC.LEFT))
INSERT = KC.TG(0)
DELETE_W = simple_key_sequence((KC.LCTRL(KC.LSHIFT(LEFT)), KC.BSPC))
CHANGE_W = simple_key_sequence((KC.LCTRL(KC.LSHIFT(LEFT)), KC.BSPC, KC.TG(0)))
WORD = simple_key_sequence((KC.LCTRL(LEFT)))
BACK = simple_key_sequence((KC.LCTRL(RIGHT)))
UNDO = KC.LCTRL(Z)
REDO = KC.LCTRL(KC.LSHIFT(Z))

combos.combos = [
        #Chord((KC.MO(1), KC.MO(2)), KC.MO(3)),
        #Chord((KC.O, KC.P), KC.BSPC),
        #Chord((KC.N0, KC.N9), KC.DEL),
        Chord((KC.LALT, KC.Q), KC.LALT(KC.TAB)),
        Chord((KC.LALT, KC.LSHIFT(KC.Q)), KC.LALT(KC.LSHIFT(KC.TAB))),

        #if keyboard.active_layers[0] == 1: (Sequence((KC.D, KC.W)),
        Sequence((KC.D, KC.W), DELETE_W),
        Sequence((KC.C, KC.W), CHANGE_W),
]

keyboard.modules = [mediakeys, rgb, encoder_handler, modtap, tapdance, combos, layers]


keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,                        KC.Y, KC.U, KC.I, KC.O, KC.P, \
        KC.A, KC.S, KC.D, KC.F, KC.G,                        KC.H, KC.J, KC.K, KC.L, KC.SCLN,  \
        KC.MT(KC.Z,KC.LSFT), KC.X, KC.C, KC.V, KC.B,         KC.N, KC.M, KC.COMMA, KC.DOT, KC.MT(KC.ENT, KC.LSFT, prefer_hold=True),  \
        KC.NO, KC.NO, KC.NO, KC.LALT, KC.TG(1),              KC.SPACE, KC.LGUI, KC.NO, KC.NO, KC.NO
    ],
    [
        KC.TRNS, WORD, KC.TRNS, REDO, KC.TRNS, KC.TRNS, UNDO, KC.TG(0), KC.TRNS, KC.TRNS, \
        KC.TG(0), KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.TRNS, \
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, \
        KC.NO  , KC.NO  , KC.NO  , KC.NO  , KC.TRNS, KC.TRNS, KC.NO  , KC.NO  , KC.NO  , KC.NO

    ]
]

# keyboard.keymap = [
#     [
#         # RAISE1
#         KC.TD(KC.Q, KC.TAB), KC.W, KC.E, KC.R, KC.T,                                KC.Y, KC.U, KC.I, KC.O, KC.TD(KC.P, KC.BSPC), \
#         KC.MT(KC.A, KC.LCTRL, prefer_hold=False), KC.S, KC.D, KC.F, KC.G,           KC.H, KC.J, KC.K, KC.L, KC.SCLN,  \
#         KC.MT(KC.Z,KC.LSFT, prefer_hold=False), KC.X, KC.C, KC.V, KC.B,             KC.N, KC.M, KC.COMMA, KC.DOT, KC.MT(KC.ENT, KC.LSFT, prefer_hold=True),  \
#         KC.NO, KC.NO, KC.NO, KC.LALT, KC.LT(2, KC.LCTRL,  prefer_hold=False),       KC.LT(1, KC.SPACE, prefer_hold=False), KC.LGUI, KC.NO, KC.NO, KC.NO
#     ],
#     [
#         # RAISE1
#         KC.LSHIFT(KC.N1), KC.LSHIFT(KC.N2), KC.LSHIFT(KC.N3), KC.LSHIFT(KC.N4), KC.LSHIFT(KC.N5),           KC.LSHIFT(KC.N6), KC.LSHIFT(KC.N7), KC.LSHIFT(KC.N8), KC.LSHIFT(KC.N9), KC.LSHIFT(KC.N0), \
#         KC.ESC,        KC.LALT,       KC.MEH,        KC.TRNS,       KC.TRNS,                                KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.QUOTE,  \
#         KC.TRNS,       KC.LCTL(KC.X), KC.LCTL(KC.C), KC.LCTL(KC.V), KC.TRNS,                                KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.SLSH,  \
#         KC.NO,         KC.NO,         KC.NO,         KC.TRNS,       KC.TRNS,                                KC.TRNS, KC.RGB_TOG, KC.NO, KC.NO, KC.NO
#     ],
#     [
#        # RAISE2
#         KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,                  KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,  \
#         KC.ESC, KC.MINUS, KC.LBRC, KC.RBRC, KC.BSLS,        KC.HOME, KC.PGDOWN, KC.PGUP, KC.END ,KC.PSCR, \
#         KC.TRNS, KC.TRNS, KC.EQUAL, KC.TRNS, KC.TRNS,       KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  \
#         KC.NO,   KC.NO,   KC.TRNS, KC.TRNS,                 KC.TRNS, KC.TRNS, KC.NO, KC.NO, KC.NO
#     ],
#     [
#         # RAISe3
#         KC.TAB, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,         KC.TRNS,  KC.TRNS, KC.TRNS, KC.DEL,   KC.BSPC,  \
#         KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,                  KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,  \
#         KC.ESC, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,         KC.F11, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,  \
#         KC.NO,   KC.NO,   KC.TRNS, KC.TRNS,                 KC.TRNS, KC.TRNS, KC.NO, KC.NO, KC.NO
#     ]
# ]




from kmk.modules.layers import Layers as _Layers
class Layers(_Layers):
    last_top_layer = 0
    hues = (4, 20, 69)

    def after_hid_send(keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            rgb.set_hsv_fill(self.hues[self.last_top_layer], 255, 255)

print('here')

if __name__ == '__main__':
    keyboard.go()
