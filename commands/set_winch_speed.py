#!/usr/bin/env python3
import wpilib
from wpilib.command import Command

class SetWinchSpeed(Command):
    def __init__(self, robot, speed):
        super().__init__()
        self.robot = robot
        self.speed = speed
        self.requires(robot.winch)

    def execute(self):
        self.robot.winch.set(self.speed)

    def isFinished(self):
        return False

    def end(self):
        self.robot.winch.set(0)

    def cancel(self):
        self.end()

def main():
    pass

if __name__ == "__main__":
    main()
