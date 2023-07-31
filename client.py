import socket
import struct
from logger import log
from types import SimpleNamespace

class Client:
    def __init__(self, IP, port, silent=False):
      self.IP = IP
      self.port = port
      self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
      print('binding to socket '+ str(self.IP) + ':' + str(self.port))
      print()
      self.socket.bind(('0.0.0.0', self.port))
      self.message=bytes([])
      self.position = 0
    def main(self):
      while (True):
        data, host = self.socket.recvfrom(2048)
        if host[0] == self.IP:
          self.message = data
          self.decode()
    def decode(self) -> SimpleNamespace:
      dataHolder = SimpleNamespace()
      try:
        dataHolder.timestamp = self.decodeNext('d')
        dataHolder.faceId = self.decodeNext('i')
        dataHolder.width = self.decodeNext('f')
        dataHolder.height = self.decodeNext('f')
        dataHolder.blink = (self.decodeNext('f'), self.decodeNext('f'))
        dataHolder.success = self.decodeNext('B')
        dataHolder.pnpError = self.decodeNext('f')
        dataHolder.faceQuat = (self.decodeNext('f'), self.decodeNext('f'), self.decodeNext('f'), self.decodeNext('f'))
        dataHolder.faceEuler = (self.decodeNext('f'), self.decodeNext('f'), self.decodeNext('f'))
        dataHolder.faceTranslation = (self.decodeNext('f'), self.decodeNext('f'), self.decodeNext('f'))
        log.print('       timestamp |', log.timestamp(dataHolder.timestamp))
        log.print('         face id |', dataHolder.faceId)
        log.print('         success |', dataHolder.success)
        log.print('       cam width |', dataHolder.width)
        log.print('      cam height |', dataHolder.height)
        log.print('           blink |', log.cleanFloatList(dataHolder.blink))
        log.print('       pnp error |', dataHolder.pnpError)
        log.print('face translation |', log.cleanFloatList(dataHolder.faceTranslation))
        log.print('  face quat ]:<  |', log.cleanFloatList(dataHolder.faceQuat))
        log.print('      face euler |', log.cleanFloatList(dataHolder.faceEuler))
      except Exception as e:
        log.print('failed message:', e)
      self.done()
      return dataHolder

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

