""" 
Python provides a socket module that provides access to the BSD socket interface. 
It includes functions and classes for creating and using sockets,
which are endpoints for communication between two machines over a network. The socket module supports various protocols,
including TCP, UDP, and raw sockets, and allows developers to create both client and server applications.
It also provides methods for sending and receiving data,
as well as for configuring socket options such as timeouts and buffer sizes.
"""

import socket

try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("www.google.com", 80))