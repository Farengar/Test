#!/usr/bin/env python3
import wpilib
from wpilib import RobotDrive
from wpilib.command import Scheduler
import oi
from subsystems.winch import Winch

class TestProgram(wpilib.SampleRobot):

    # Wheel channels
    kFrontLeftChannel = 0
    kRearLeftChannel = 1
    kFrontRightChannel = 2
    kRearRightChannel = 3

    def robotInit(self):
        '''Robot initialization function'''

        self.robotDrive = wpilib.RobotDrive(self.kFrontLeftChannel,
                                            self.kRearLeftChannel,
                                            self.kFrontRightChannel,
                                            self.kRearRightChannel)

        self.robotDrive.setExpiration(0.1)

        # invert left side motors
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontLeft, True)
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kRearLeft, True)
        self.winch = Winch(self)
        self.oi = oi.OI(self)

    def operatorControl(self):
        '''Runs the motors with Mecanum drive.'''

        self.robotDrive.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():

            Scheduler.getInstance().run()

            self.robotDrive.mecanumDrive_Cartesian(self.oi.stick.getX(),
                                                   self.oi.stick.getY(),
                                                   self.oi.stick.getZ(), 0);

            wpilib.Timer.delay(0.005) # wait 5ms to avoid hogging CPU cycles

def main():
    wpilib.run(TestProgram)

if __name__ == "__main__":
    main()
