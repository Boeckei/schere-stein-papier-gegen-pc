Punkte = 0
zeichen = 0

def on_button_a():
    global Punkte
    Punkte += 1
    if Punkte == 1:
        basic.set_led_color(0xff0000)
    elif Punkte == 2:
        basic.set_led_color(0xff8000)
    elif Punkte == 3:
        basic.set_led_color(0xffff00)
    else:
        basic.set_led_color(0x00ff00)
        music.play_melody("F - G - A - F - ", 250)
        music.play_melody("A - G - G - C - ", 250)
        music.play_melody("F - G - A - F - ", 250)
        music.play_melody("A - G - G - C - ", 250)
        music.play_melody("F - G - A - F - ", 250)
        music.play_melody("A - G - G - C - ", 250)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    global Punkte
    Punkte = 0
    basic.show_number(0)
    basic.set_led_color(0xff0000)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_gesture_shake():
    global zeichen
    zeichen = randint(1, 3)
    if zeichen == 1:
        basic.show_icon(IconNames.SQUARE)
    elif zeichen == 2:
        basic.show_icon(IconNames.SMALL_SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
