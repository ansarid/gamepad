# gamepad
My gamepad library

## Example

```
#!/usr/bin/python3

from time import sleep
import gamepad

controller = gamepad.Controller(0)

while True:

    button = controller.get_buttons()
    joystick = controller.get_joysticks()
    trigger = controller.get_triggers()

    if controller.mode:

        if button['a']:

            controller.rumble(10, 1)       # This function may require root. If no rumble is observed run program with sudo.

        if button['b']:

            controller.rumble(100, 1)       # This function may require root. If no rumble is observed run program with sudo.

        if button['x']:

            controller.buzz(1)              # This function may require root. If no rumble is observed run program with sudo.

        if button['y']:

            controller.buzz(3)              # This function may require root. If no rumble is observed run program with sudo.

        print(button)
        # print(button['a'], button['b'], button['x'], button['y'])

        # print(joystick)

        # print(trigger)

    else:

        print("Error: Controller in incorrect mode!")
        controller.reset()

    sleep(0.01)

```
