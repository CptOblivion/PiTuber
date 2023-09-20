import sys, os, argparse
from client import Client

defaultIP = "127.0.0.1"
defaultPort = 11573

if __name__ == '__main__':
  address = defaultIP
  port = defaultPort

  parser = argparse.ArgumentParser()
  parser.add_argument('-a', '--address')
  parser.add_argument('-m', '-mute', action='store_true')
  parser.add_argument('-l', '-local', action='store_true')
  args = parser.parse_args()
  if args.address is not None:
    address = args.address
    if ':' in address:
      [address, port] = address.split(':')
      if address == '' or address == 'localhost':
        # allow for assigning just port
        address = defaultIP
      port = int(port)
  client = Client(address, port, args.local)
  try:
    client.main()
  except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(130)
    except SystemExit:
        os._exit(130)