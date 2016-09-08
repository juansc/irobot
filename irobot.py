import struct
import sys
import glob  # for listing serial ports
import time

import ports as p
import commands as c
from logging import *

try:
    import serial
except ImportError:
    raise


def main():
    connection = connect_to_robot()
    commander = c.iRobotInterface(connection)

    reset_robot()

    log_message("Routine will run now")
    while True:
        commander.beep(connection)
        time.sleep(5)

    loop()


def reset_robot():
    # Sometimes the robot won't move until it
    # is first in passive mode and then safe mode.
    # To fix this, we go first into passive then safe mode.
    commander.enter_passive_mode()
    commander.enter_safe_mode()


def connect_to_robot():
    ports = p.get_serial_ports()
    port = p.choose_port(ports)
    connection = p.connect_to_port(port)
    return connection


if __name__ == "__main__":
    init()
