import socket
import ipaddress
import argparse
import json

def scan_host(host, port):
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(1)