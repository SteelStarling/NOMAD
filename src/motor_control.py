"""Motor controller code for RasPi GPIO
Author: Taylor Hancock
Date:   04/04/2025
Class:  AE445 - Spacecraft Detail Design
Assignment: NOMAD
"""

from time import sleep

from gpiozero import Device, PhaseEnableMotor, Servo, RotaryEncoder, Button
from gpiozero.tools import sin_values, cos_values
from gpiozero.pins.mock import MockFactory, MockPWMPin
import yaml

from gpio_const import GPIO_EXISTS

MOTOR_CONFIG = "motor_config.yaml"

MOTOR_STEPS = 1
ENCODER_STEPS = 4000


def parse_config(config_file: str = MOTOR_CONFIG) -> object | None:
    """Reads in a config file in yaml format to an object"""
    with open(config_file, encoding='utf-8') as conf:
        try:
            motor_values = yaml.safe_load(conf)
            return motor_values
        except yaml.YAMLError as e:
            print(f"YAML Error: {e}")

    return None


def create_reset_encoder(encoder: RotaryEncoder) -> callable:
    """Creates a reset encoder function for the provided encoder"""
    def reset_encoder() -> None:
        """Resets the given encoder to 0"""
        nonlocal encoder
        encoder.value = 0

    return reset_encoder


def spin_motor(motor: PhaseEnableMotor, speed: float, dir: bool = True) -> None:
    """Spins the given motor at the given speed"""


def servo_open(servo: Servo) -> None:
    """Opens the given servo smoothly"""
    print(servo.source)
    servo.source = sin_values()
    sleep(1.8)
    servo.source = None
    servo.value = 1

def servo_close(servo: Servo) -> None:
    """Closes the given servo smoothly"""
    servo.source = cos_values()
    sleep(1.8)
    servo.source = None
    servo.value = -1


def create_motor(motor_data: dict) -> PhaseEnableMotor:
    """Creates a motor from the given dictionary"""
    return PhaseEnableMotor(motor_data["dir"], motor_data["step"])

def create_encoder(motor_data: dict) -> RotaryEncoder:
    """Creates a z-pulse encoder
    
    NOTES: So, what *is* a Z-Pulse Encoder?
    It's just a normal encoder, but with Z-Pulse
    Z turns to high when the initial ("zero position") value is encountered
    Very good for homing
    """

    # Set so when z_pulse happens, the encoder is reset
    encoder = RotaryEncoder(motor_data["encoder_a"], motor_data["encoder_b"])

    z_pulse = Button(motor_data["encoder_z"])
    z_pulse.when_pressed = create_reset_encoder(encoder)


if __name__ == "__main__":
    config_data = parse_config()

    # When testing on devices without GPIO, create fake pins to test with
    if not GPIO_EXISTS:
        Device.pin_factory = MockFactory(pin_class=MockPWMPin)

    # Create sub dictionaries for easier access
    motor_data = config_data["motors"]
    servo_data = config_data["servos"]

    debris_motor = create_motor(motor_data["debris"])
    # debris_encoder = 
    reel_motor = create_motor(motor_data["reel"])
    tensioning_motor = create_motor(motor_data["tensioning"])
    lid_servo = Servo(
        servo_data["lid"]["pwm"],
        initial_value=1,
        min_pulse_width=0.0004,
        max_pulse_width=0.00205,
        frame_width=0.003
    )

    print("Manual Lid Control")
    for _ in range(0):
        lid_servo.min()
        sleep(1)
        lid_servo.mid()
        sleep(1)
        lid_servo.max()
        sleep(1)

    print("Opening Lid")
    servo_open(lid_servo)
    sleep(10)
    #print("Closing Lid")
    #servo_close(lid_servo)
