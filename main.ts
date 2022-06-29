input.onButtonPressed(Button.A, function () {
    num += 1
    whaleysans.showNumber(num)
})
input.onButtonPressed(Button.AB, function () {
    num += 10
    whaleysans.showNumber(num)
})
input.onButtonPressed(Button.B, function () {
    while (num >= 0) {
        whaleysans.showNumber(num)
        basic.pause(1000)
        num += -1
    }
    basic.showLeds(`
        # # . # #
        # # . # #
        # # . # #
        # # . # #
        # # . # #
        `)
    music.playSoundEffect(music.createSoundEffect(WaveShape.Noise, 1957, 3785, 255, 255, 2500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    basic.clearScreen()
})
let num = 0
num = 0
