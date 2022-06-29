def on_button_pressed_a():
    global _2
    _2 += 1
    whaleysans.show_number(_2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global _2
    while _2 >= 0:
        whaleysans.show_number(_2)
        basic.pause(500)
        _2 += -1
    basic.show_leds("""
        # # . # #
                # # . # #
                # # . # #
                # # . # #
                # # . # #
    """)
    music.play_sound_effect(music.create_sound_effect(WaveShape.NOISE,
            1957,
            3785,
            255,
            255,
            2500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

_2 = 0
_2 = 0