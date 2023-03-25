import socket

trackerIP = "127.0.0.1"
trackerPort = 11573
bufferSize = 1024

class Client:
    def __init__(self):
      self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    def main(self):
       while True:
          data, addr = self.socket.recvfrom(bufferSize)
          print(data)