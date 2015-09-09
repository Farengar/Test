#!/usr/bin/env python3
import wpilib
from wpilib.command import Subsystem
from commands.set_winch_speed import SetWinchSpeed

class Winch(Subsystem):
    kStop = 0
    kForward = 1
    kBackward = -1

    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.motor = wpilib.Talon(4)

    def set(self, speed):
        self.motor.set(speed)

def main():
    pass

if __name__ == "__main__":
    main()
