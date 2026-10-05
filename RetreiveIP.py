import socket

try:
    ip = socket.gethostbyname("google.com")
    print(ip)
except socket.gaierror:
    print("Failed to retrieve IP address for google.com")