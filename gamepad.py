#!/usr/bin/python3

#   Import libraries

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import time
import pygame                                   # Using to get data from gamepad controller.
import usb.core                                 # Using to check controller mode
import subprocess
# import pygame.joystick


def no_display():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'     # Create "dummy display" for pygame.
    pygame.display.set_mode((1, 1))             # Set display mode.
    # pygame.init()                               # Start pygame.


class Controller:

    def __init__(self, controller, idVendor=0x45e, idProduct=0x28e):
        pygame.init()
        pygame.joystick.init()

        self.controller = controller

        self.idVendor = idVendor
        self.idProduct = idProduct

        self.last_rumble = 0
        self.last_buzz = 0

        self.last_rumble_duration = 0
        self.last_buzz_duration = 0

        self.setup()

    def setup(self):
        self.joystick_count = pygame.joystick.get_count()
        if self.joystick_count > 0:
            self.joystick = pygame.joystick.Joystick(self.controller)
            self.joystick.init()
            self.name = self.joystick.get_name()
            self.check_mode()
        else:
            pass

    def check_mode(self):
        dev = usb.core.find(find_all=True)
        for info in dev:
            if info.idProduct == self.idProduct and info.idVendor == self.idVendor:
                self.mode = 1
                break
            else:
                self.mode = 0

    def get_joysticks(self):
        self.check_mode()
        pygame.event.get()
        if self.mode:
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
        else:
            return 1

    def get_triggers(self):
        self.check_mode()
        pygame.event.get()
        if self.mode:
            self.triggers = {
                            "rt": round(self.joystick.get_axis(5), 3),
                            "lt": round(self.joystick.get_axis(2), 3)
                        }
            return self.triggers
        else:
            return 1

    def get_buttons(self):
        self.check_mode()
        pygame.event.get()
        if self.mode:
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
        else:
            return 1

    def rumble(self, power, duration):
        if (time.time() - self.last_rumble) >= self.last_rumble_duration:
            self.last_rumble = time.time()
            self.last_rumble_duration = duration
            if self.mode:
                duration *= 1000
                subprocess.Popen(['./rumble_c/rumble', str(self.controller), str(power), str(0), str(duration)], stdout=subprocess.PIPE)
            else:
                print("ERROR: This mode does not allow use of the rumble.")
        else:
            return 1    # Last rumble is still in progress

    def buzz(self, duration):
        if (time.time() - self.last_buzz) >= self.last_buzz_duration:
            self.last_buzz = time.time()
            self.last_buzz_duration = duration
            if self.mode:
                duration *= 1000
                subprocess.Popen(['./rumble_c/rumble', str(self.controller), str(0), str(100), str(duration)], stdout=subprocess.PIPE)
            else:
                print("ERROR: This mode does not allow use of the buzzer.")
        else:
            return 1    # Last rumble is still in progress

    def reset(self):
        pygame.joystick.quit()
        pygame.joystick.init()
        self.setup()
