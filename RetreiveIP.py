import socket

try:
    ip = socket.gethostbyname("google.com")
    print(ip)