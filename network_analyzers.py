import socket
import ipaddress
import argparse
import json

def scan_host(host, port):
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(1)
        result = connection.connect_ex((host, port))
        connection.close()
        return result == 0
    except socket.error:
        return False
    
    
def analyze_host(host):
    try:
        ip = ipaddress.ip_address(socket.gethostbyname(host))
        ports = [21, 22, 80, 443, 3306, 8080]
        results = {}
        for port in ports:
            results[str(port)] = scan_host(str(ip), port)
        return {
            "hostname": host,
            "ip_address": str(ip),
            "version": ip.version,
            "is_private": ip.is_private,
            "open_ports": [p for p, opened in results.items() if opened],
            "port_scan": results
            }