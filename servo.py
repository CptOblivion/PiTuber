from adafruit_servokit import ServoKit
import util

servoRange = 160
channelCount = 16

class Servo:
  def __init__(self) -> None:
    self.kit = ServoKit(channels=channelCount)
    for i in range(channelCount):
       self.kit.servo[i].actuation_range = servoRange

  def sendPosition(self, motor, left, right, val):
      # TODO: allow custom servo limits
      outval = util.mapRange(left, right, val, servoRange)
      self.kit.servo[motor].angle = outval