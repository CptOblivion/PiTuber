import socket, sys, os

defaultIP = "127.0.0.1"
defaultPort = 11573
bufferSize = 1024

class Client:
    def __init__(self, IP, port):
      self.IP = IP
      self.port = port
      self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
      self.socket.bind((defaultIP, self.port))
      print("initialized on IP", self.IP, "port", self.port)
    def main(self):
       while True:
        data, addr = self.socket.recvfrom(bufferSize)
        print(addr, ":", "{}".format(data[0]))

if __name__ == "__main__":
  IP = defaultIP
  port = defaultPort
  if len(sys.argv) > 1:
    try:
      port = int(sys.argv[1])
    except ValueError:
      print("invalid port", sys.argv[1])
  client = Client(IP, port)
  try:
    client.main()
  except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(130)
    except SystemExit:
        os._exit(130)