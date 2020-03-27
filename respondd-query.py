from socket import socket, AF_INET6, SOCK_DGRAM
import zlib
import sys

s = socket(AF_INET6, SOCK_DGRAM)
s.bind(('::', 14233))
s.sendto("GET {name}".format(name=sys.argv[2]).encode(), (sys.argv[1], 1001))
data, addr = s.recvfrom(2048)
d = zlib.decompress(data, wbits=-zlib.MAX_WBITS)
print(d.decode())
