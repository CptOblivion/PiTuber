import serial
from logger import log
import util

class Coms:
    def __init__(self) -> None:
        # TODO: optional port override
        self.scanPorts()

    def scanPorts(self):
        for i in range(10):
            self.port = "COM" + str(i)
            if self.__connect():
                return
        raise Exception("could not find port")

    def __connect(self):
        try:
            self._ser = serial.Serial(self.port, 9600)
            return True
        except serial.SerialException as e:
            e = str(e)
            if "FileNotFoundError" in e:
                log.print("invalid connection:", e)
                return
            log.print("unhandled error:", e)
            return

    def sendPosition(self, motor, left, right, val):
        # TODO: allow custom servo limits
        val = util.mapRange(left, right, val, 1)
        log.print("servo ", motor, " val: ", log.cleanFloat(val), " actual ", int(val * 0xfe))
        try:
            self._ser.write([motor, int(val * 0xfe), 0xff])
        except:
            # retry connection once
            self.__connect()