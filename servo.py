from adafruit_servokit import ServoKit
from logger import log

range = 160

class Servo:
  def __init__(self) -> None:
    self.kit = ServoKit(channels=16)
    for i in range(16):
       self.kit.servo[i].actuation_range = range

  def sendPosition(self, motor, left, right, val):
      # TODO: allow custom servo limits
      val = mapRange(left, right, val)
      log.print("servo ", motor, " val: ", log.cleanFloat(val), " actual ", int(val * 0xfe))
      self.kit.servo[motor].angle = val


def mapRange(left, right, val):
  return min(1, max(0, (val - left) / (right - left))) * range