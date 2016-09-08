import struct

import serial
from logging import *

class iRobotInterface(object):
    """docstring for iRobotInterface"""
    def __init__(self, connection):
        super(iRobotInterface, self).__init__()
        self.connection = connection

    def beep(self, connection):
        cmd = struct.pack(">Bhh", 145, 200, 200)
        print cmd
        self.sendCommandRaw(cmd)
        log_message('Beeped')
        log_message('Sent {}'.format(cmd))

    def enter_passive_mode(self):
        self.sendCommandASCII('128')
        log_message("Entered Passive Mode")
        log_message("Sent {}".format('128'))


    def enter_safe_mode(self):
        self.sendCommandASCII('131')
        log_message("Entered safe Mode")
        log_message("Sent {}".format('131'))

    def sendCommandASCII(self, command):
        cmd = ""
        for v in command.split():
            cmd += chr(int(v))

        self.sendCommandRaw(cmd)

    # sendCommandRaw takes a string interpreted as a byte array
    def sendCommandRaw(self, command):

        try:
            if self.connection is not None:
                # Writes to iRobot
                self.connection.write(command)
            else:
                # Says it's not connected
                print "Not connected."
        except serial.SerialException:
            print "Lost connection"
            self.connection = None