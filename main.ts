let Punkte = 0
let zeichen = 0
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    Punkte += 1
    if (Punkte == 1) {
        basic.setLedColor(0xff0000)
    } else if (Punkte == 2) {
        basic.setLedColor(0xff8000)
    } else if (Punkte == 3) {
        basic.setLedColor(0xffff00)
    } else {
        basic.setLedColor(0x00ff00)
        music.playMelody("F - G - A - F - ", 250)
        music.playMelody("A - G - G - C - ", 250)
        music.playMelody("F - G - A - F - ", 250)
        music.playMelody("A - G - G - C - ", 250)
        music.playMelody("F - G - A - F - ", 250)
        music.playMelody("A - G - G - C - ", 250)
    }
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    Punkte = 0
    basic.showNumber(0)
    basic.setLedColor(0xff0000)
})
input.onGesture(Gesture.Shake, function () {
    zeichen = randint(1, 3)
    if (zeichen == 1) {
        basic.showIcon(IconNames.Square)
    } else if (zeichen == 2) {
        basic.showIcon(IconNames.SmallSquare)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
