#!/usr/bin/python3

#   Import libraries

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame                                   # Using to get data from gamepad controller.
import subprocess

def no_display():

    os.environ['SDL_VIDEODRIVER'] = 'dummy'     # Create "dummy display" for pygame.
    pygame.display.set_mode((1, 1))             # Set display mode.
    pygame.init()                               # Start pygame.


class Controller:

    def __init__(self, controller):

        pygame.init()
        pygame.joystick.init()

        self.controller = controller

        self.joystick_count = pygame.joystick.get_count()

        # self.analog_sticks = None
        # self.triggers = None
        # self.buttons = None

        if self.joystick_count > 0:

            self.joystick = pygame.joystick.Joystick(self.controller)
            self.joystick.init()

            self.name = self.joystick.get_name()

        else:

            pass

    def get_joysticks(self):

        pygame.event.get()

        self.analog_sticks = {
                    "left": {
                        "x": round(self.joystick.get_axis(0), 3),
                        "y": round(self.joystick.get_axis(1), 3) * -1
                        },
                    "right": {
                        "x": round(self.joystick.get_axis(3), 3),
                        "y": round(self.joystick.get_axis(4), 3) * -1
                        }
                    }

        return self.analog_sticks

    def get_triggers(self):

        pygame.event.get()

        self.triggers = {
                    "rt": round(self.joystick.get_axis(5), 3),
                    "lt": round(self.joystick.get_axis(2), 3)
                    }

        return self.triggers

    def get_buttons(self):

        pygame.event.get()

        buttons = {
                    "dpad": self.joystick.get_hat(0),
                    "joystick": {
                        "left": self.joystick.get_button(9),
                        "right": self.joystick.get_button(10)
                        },
                    "a": self.joystick.get_button(0),
                    "b": self.joystick.get_button(1),
                    "x": self.joystick.get_button(2),
                    "y": self.joystick.get_button(3),
                    "lb": self.joystick.get_button(4),
                    "rb": self.joystick.get_button(5),
                    "home": self.joystick.get_button(8),
                    "back": self.joystick.get_button(6),
                    "start": self.joystick.get_button(7),
                    }

        return buttons

    def rumble(self, power, duration):
        if self.name != "Microsoft X-Box 360 Pad":
            duration *= 1000
            subprocess.Popen(['./rumble_c/rumble', str(self.controller), str(power), str(0), str(duration)], stdout=subprocess.PIPE)
        else:
            print("ERROR: This mode does not allow rumble.")

    def buzz(self, duration):
        if self.name != "Microsoft X-Box 360 Pad":
            duration *= 1000
            subprocess.Popen(['./rumble_c/rumble', str(self.controller), str(0), str(100), str(duration)], stdout=subprocess.PIPE)
        else:
            print("ERROR: This mode does not allow the buzzer.")
