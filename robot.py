#!/usr/bin/env python3
import wpilib
from wpilib import RobotDrive

class TestProgram(wpilib.SampleRobot):
    
    # Wheel channels
    kFrontLeftChannel = 4
    kRearLeftChannel = 3
    kFrontRightChannel = 8
    kRearRightChannel = 4
    
    # Joystick channel
    joystickChannel = 0
    
    def robotInit(self):
        '''Robot initialization function'''
        
        self.robotDrive = wpilib.RobotDrive(self.kFrontLeftChannel,
                                            self.kRearLeftChannel,
                                            self.kFrontRightChannel,
                                            self.kRearRightChannel)

        self.robotDrive.setExpiration(0.1)
        
        # invert left side motors
        self.robotDrive.setInvertedMotor(RobotDrive.MotorType.kFrontLeft, True)
        
        # possibly needs changed
        self.robotDrive.setInvertedMotor(RobotDrive.MotoorType.kRearLeft, True)
        
        self.stick = wpilib.Joystick(self.joystickChannel)
        
    def operatorControl(self):
        '''Runs the motors with Mecanum drive.'''
    
        self.robotDrive.setSafetyEnabled(True)
        while self.isOperatorControl() and self.isEnabled():
            
            self.robotDrive.meanumDrive_Cartesian(self.stick.getX(),
                                                  self.stick.getY(),
                                                  self.stick.getZ(), 0);
            wpilib.Timer.delay(0.005) # wait 5ms to avoid hogging CPU cycles

def main():
    wpilib.run(TestProgram)

if __name__ == "__main__":
    main()
