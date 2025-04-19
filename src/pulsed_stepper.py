"""Creates a pulsed stepper motor for use with a DRV8825
Author: Taylor Hancock
Date:   04/19/2025
Class:  AE445 - Spacecraft Detail Design
Assignment: NOMAD
"""

from gpiozero import PWMOutputDevice, DigitalOutputDevice

class PulsedStepperMotor:

    # hardcodes PWM to 50% duty cycle
    PWM_PERCENT = 0.5

    def __init__(self, step_pin: int, direction_pin: int, enable_pin: int):
        """Creates a pulsed stepper motor with the given step/drive pin, direction pin, and enable pin"""
        self.step_control = PWMOutputDevice(step_pin)
        self.direction_control = DigitalOutputDevice(direction_pin)
        self.enable_control = DigitalOutputDevice(enable_pin)


    def run_motor(self, freq: int = 1000, forward: bool = True) -> None:
        """Runs the given motor"""
        # set direction
        if forward:
            self.direction_control.on()
        else:
            self.direction_control.off()
        
        # enable motor
        self.enable_control.on()

        # start moving at frequency
        self.step_control.on()
        self.step_control.value = PulsedStepperMotor.PWM_PERCENT
        self.step_control.frequency = freq


    def stop(self) -> None:
        """Stops the given motor"""
        # stop motor
        self.step_control.frequency = 0
        self.step_control.off()

        # disable motor
        self.enable_control.off()