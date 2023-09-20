import servo, coms
from datetime import datetime
import threading, time

motorCount = 16

class Driver:
  def __init__(self, local) -> None:
    if local:
      self.target = servo.Servo()
    else:
      self.target = coms.Coms()
    self.motors = [None] * motorCount
    main = threading.Thread(target = self._main)
    main.start()
    pass

  def sendPosition(self, motorIndex, left, right, val):
    if self.motors[motorIndex] is None:
      self.motors[motorIndex] = Motor(self.target, left, right, motorIndex)
    self.motors[motorIndex].setPos(val)

  def _main(self):
    for motor in self.motors:
      if motor is None:
        continue
      motor.update()
    time.sleep(0.05)

class Motor:
  def __init__(self, target, left, right, index) -> None:
    self.target = target
    self.left = left
    self.right = right
    self.index = index
    self.value = 0.5
    self.fromTime = datetime.now()
    self.fromPos = 0.5
    self.toPos = None
    self.toTime = None
    self.dur = None
    pass
  def setPos(self, value):
    now = datetime.now()
    self.fromPos = self.value
    self.toPos = value
    #get diff of now and last update, to determine toTime
    self.toTime = now - self.fromTime
    self.fromTime = now

  def update(self):
    now = datetime.now()
    # get lerp pos
    dur = self.toTime - self.fromTime
    t = max(0, min(1, (self.fromTime - now) / dur))
    # lerp
    self.value = (self.toPos * t) + ((1 - t) * self.fromPos)
    self.target.sendPosition(self.index, self.left, self.right, self.value)