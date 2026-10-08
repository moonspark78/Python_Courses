from operator import ge

import shapely

while True:
    try:
        ip = socket.gethostbyname("google.com")
        print(ip)
    except socket.gaierror:
        print("Failed to retrieve IP address for google.com")


if __name__ == "__main__":
    try:
        ip = socket.gethostbyname("google.com")
        print(ip)
    except socket.gaierror:
        print("Failed to retrieve IP address for google.com")
        
        

def get_ip_address(hostname):
