import sys
from datetime import datetime

class log:
  __lines = []
  __resetWidth = 0
  __resetHeight = 0
  __mute = False

  def mute(mute: bool):
    log.__mute = mute

  def print(*args):
    if log.__mute:
      return
    message = ''
    for arg in args:
      message += ' ' + str(arg)
    if not message.endswith('\n'):
      message += '\n'
    log.__lines.append(message)

  def send():
    if log.__mute:
      return
    # clear first
    resetString = ''
    for _ in range(log.__resetWidth):
      resetString += ' '
    for _ in range(log.__resetHeight):
      sys.stdout.write(resetString + '\033[F') # up a line

    log.__resetWidth = 0
    log.__resetHeight = 0

    for line in log.__lines:
      for subline in  line.split('\n'):
        log.__resetWidth = max(log.__resetWidth, len(subline))
        log.__resetHeight += 1
      sys.stdout.write(line)
    sys.stdout.write('\r') # start of the line
    log.__lines = [] # reset
    sys.stdout.flush()

  def cleanFloatList(floatlist):
    return '[ ' + ' | '.join(format(f, '+1.3f') for f in floatlist) + ' ]'

  def timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')