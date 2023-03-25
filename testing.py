import socket

trackerIP = "127.0.0.1"
trackerPort = 11573
bufferSize = 1024

class Client:
    def __init__(self):
      self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
      self.socket.bind((trackerIP, trackerPort))
      print("initialized")
    def main(self):
       while True:
          data, addr = self.socket.recvfrom(bufferSize)
          print(data)

if __name__ == "__main__":
   client = Client()
   client.main()