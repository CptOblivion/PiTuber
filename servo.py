from adafruit_servokit import ServoKit
from logger import log
import util

range = 160

class Servo:
  def __init__(self) -> None:
    self.kit = ServoKit(channels=16)
    for i in range(16):
       self.kit.servo[i].actuation_range = range

  def sendPosition(self, motor, left, right, val):
      # TODO: allow custom servo limits
      val = util.mapRange(left, right, val, range)
      log.print("servo ", motor, " val: ", log.cleanFloat(val), " actual ", int(val * 0xfe))
      self.kit.servo[motor].angle = val