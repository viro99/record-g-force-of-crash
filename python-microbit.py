g = 0
crashForce = 0

def on_button_pressed_a():
    basic.show_number(g)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(crashForce)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global g, crashForce
    g = Math.sqrt(input.acceleration(Dimension.X) ** 2 + (input.acceleration(Dimension.Y) ** 2 + input.acceleration(Dimension.Z) ** 2))
    if g > crashForce:
        crashForce = g
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
