import struct
import sys
import glob  # for listing serial ports
from logging import *

try:
    import serial
except ImportError:
    raise

def choose_port(ports):
    if len(ports) is 0:
        print_error_message_and_exit("No ports found")

    print "Please choose the port to connect to: "
    for num, port in enumerate(ports):
        print "    Port[{}] : {}".format(num + 1, port)

    try:
        port_num = int(input("Port: "))
        if port_num < 1 or port_num > len(ports):
            print_error_message_and_exit(
                "Invalid input. Must select a number from {} to {}".format(1, len(ports)))
    except (ValueError, NameError):
        print_error_message_and_exit(
            "Invalid input. Must select a number from {} to {}.".format(1, len(ports)))

    return ports[port_num - 1]


def connect_to_port(port):
    if port is None:
        print_error_message_and_exit("No port to check")

    print "Attempting to connect to {}... ".format(port)
    connection = None
    try:
        connection = serial.Serial(port, baudrate=115200, timeout=1)
        print "Successfully connected to {}".format(port)
    except:
        print_error_message_and_exit("Failed to connect to port {}.".format(port))

    return connection


def get_serial_ports():
    """Lists serial ports
    From http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    print "Looking for ports to connect to..."
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result