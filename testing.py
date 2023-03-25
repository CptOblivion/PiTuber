import socket, sys, os

defaultIP = "127.0.0.1"
defaultPort = 11573
bufferSize = 1024

class Client:
    def __init__(self, IP, port):
      self.IP = IP
      self.port = port
      self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
      # print("connecting to socket: IP", self.IP, "port", self.port)
      # self.socket.connect((self.IP, self.port))
    def main(self):
       while True:
        chunks = []
        while True:
          data, server = self.socket.recvfrom(bufferSize)
          if not data:
            break
          print(server)
          chunks.append(data)
        print(b''.join(chunks))

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