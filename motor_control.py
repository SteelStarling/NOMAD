"""Motor controller code for RasPi GPIO
Author: Taylor Hancock
Date:   04/04/2025
Class:  AE445 - Spacecraft Detail Design
Assignment: NOMAD
"""

from time import sleep

from gpiozero import Device, PhaseEnableMotor, Servo, RotaryEncoder, Button
from gpiozero.pins.mock import MockFactory
import yaml

MOTOR_CONFIG = "motor_config.yaml"

GPIO_EXISTS = False


def parse_config(config_file: str = MOTOR_CONFIG) -> object | None:
    """Reads in a config file in yaml format to an object"""
    with open(config_file, encoding='utf-8') as conf:
        try:
            motor_values = yaml.safe_load(conf)
            return motor_values
        except yaml.YAMLError as e:
            print(f"YAML Error: {e}")

    return None

def spin_motor(motor: PhaseEnableMotor, speed: float, dir: bool = True) -> None:
    """Spins the given motor at the given speed"""


def spin_servo(servo_pin: int, angle: float) -> None:
    """Spins the given servo to the specified angle"""

def read_encoder(encoder: RotaryEncoder, z_pulse: Button) -> float:
    """Calculates the position of a given encoder"""

    # So, what *is* a Z-Pulse Encoder?
    #
    # It's just a normal encoder, but with Z-Pulse\
    # Z turns to high when the initial ("zero position") value is encountered
    # Very good for homing




if __name__ == "__main__":
    config_data = parse_config()

    # When testing on devices without GPIO, create fake pins to test with
    if GPIO_EXISTS:
        Device.pin_factory = MockFactory()

    motor_data = config_data["motors"]

    servo_data = config_data["servos"]

    lid_servo = Servo(servo_data["lid"]["pwm"])

    while True:
        lid_servo.min()
        sleep(1)
        lid_servo.mid()
        sleep(1)
        lid_servo.max()
        sleep(1)
