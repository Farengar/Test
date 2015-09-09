#!/usr/bin/env python3
import wpilib
from wpilib.buttons import JoystickButton
from commands.set_winch_speed import SetWinchSpeed

class OI:
    def __init__(self, robot):
        self.stick = wpilib.Joystick(0)
        self.button_forward = JoystickButton(self.stick, 1)
        self.button_back = JoystickButton(self.stick, 2)

        self.button_forward.whileHeld(SetWinchSpeed(robot, robot.winch.kForward))
        self.button_back.whileHeld(SetWinchSpeed(robot, robot.winch.kBackward))

def main():
    pass

if __name__ == "__main__":
    main()
