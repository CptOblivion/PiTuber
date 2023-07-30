import socket, sys, os
import struct
from logger import log

defaultIP = "127.0.0.1"
defaultPort = 11573

class Client:
    def __init__(self, IP, port):
      self.IP = IP
      self.port = port
      self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
      print('binding to socket '+ str(self.IP) + ':' + str(self.port))
      print()
      self.socket.bind((self.IP, self.port))
      self.message=bytes([])
      self.position = 0
    def main(self):
      while (True):
        data, host = self.socket.recvfrom(2048)
        if host[0] == self.IP:
          self.message = data
          self.decode()
    def decode(self):
      try:
        timestamp = self.decodeNext('d')
        faceId = self.decodeNext('i')
        width = self.decodeNext('f')
        height = self.decodeNext('f')
        blink = (self.decodeNext('f'), self.decodeNext('f'))
        success = self.decodeNext('B')
        pnpError = self.decodeNext('f')
        faceQuat = (self.decodeNext('f'), self.decodeNext('f'), self.decodeNext('f'), self.decodeNext('f'))
        faceEuler = (self.decodeNext('f'), self.decodeNext('f'), self.decodeNext('f'))
        faceTranslation = (self.decodeNext('f'), self.decodeNext('f'), self.decodeNext('f'))
        log.print('       timestamp |', log.timestamp(timestamp))
        log.print('         face id |', faceId)
        log.print('         success |', success)
        log.print('       cam width |', width)
        log.print('      cam height |', height)
        log.print('           blink |', log.cleanFloatList(blink))
        log.print('       pnp error |', pnpError)
        log.print('face translation |', log.cleanFloatList(faceTranslation))
        log.print('  face quat ]:<  |', log.cleanFloatList(faceQuat))
        log.print('      face euler |', log.cleanFloatList(faceEuler))
      except Exception as e:
        log.print('failed message:', e)
      self.done()

    def decodeNext(self, format):
      chunksize = struct.calcsize(format)
      if len(self.message) < self.position + chunksize - 1:
        return "end of bytes reached"
      val = struct.unpack(format, self.message[self.position:self.position+chunksize])
      self.position += chunksize
      return val[0]

    def done(self):
      log.print('unread bytes: ', len(self.message) - self.position)
      log.send()
      self.resetMessage()


    def resetMessage(self):
      self.message=bytes([])
      self.position = 0


if __name__ == '__main__':
  address = defaultIP
  port = defaultPort
  if len(sys.argv) > 1:
    address = sys.argv[1]
    if ':' in address:
      [address, port] = address.split(':')

      if address == '' or address == 'localhost':
        # allow for assigning just port
        address = defaultIP
      port = int(port)
  client = Client(address, port)
  try:
    client.main()
  except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(130)
    except SystemExit:
        os._exit(130)