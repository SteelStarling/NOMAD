"""Motor controller code for RasPi GPIO
Author: Taylor Hancock
Date:   04/04/2025
Class:  AE445 - Spacecraft Detail Design
Assignment: NOMAD
"""

from time import sleep

import gpiozero
import yaml

MOTOR_CONFIG = "motor_config.yaml"



def parse_config(config_file: str = MOTOR_CONFIG) -> object | None:
    """Reads in a config file in yaml format to an object"""
    with open(config_file, encoding='utf-8') as conf:
        try:
            motor_values = yaml.safe_load(conf)
            return motor_values
        except yaml.YAMLError as e:
            print(f"YAML Error: {e}")

    return None


def spin_motor(motor_pin: int, freq: int, steps: int, dir: bool = True) -> None:
    """Spins the given motor at the given Hz rate"""
    sleep_time = 1 / freq



    for _ in range(steps):
        
        sleep(sleep_time)
    


def spin_servo(servo_pin: int, angle: float) -> None:
    """Spins the given servo to the specified angle"""


def read_encoder(enc_p1: int, enc_p2: int, enc_p3: int) -> float:
    """Calculates the position of a given encoder"""


if __name__ == "__main__":
    config_data = parse_config()

    print(config_data)

    print("A")