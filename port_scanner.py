
# ----------------------------------------
# Port Scanner Script
# Author: Deqa Mohamed
# GitHub: https://github.com/Deqa2020
# LinkedIn: https://www.linkedin.com/in/deqa-mohamed-13149a23b/
# Description: Simple Python script to scan open ports on a host
# ----------------------------------------

import socket
from datetime import datetime

# Get user input
target = input("Enter target IP address or domain: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print(f"\nStarting scan on {target}")
print(f"Scanning ports {start_port} to {end_port}...\n")
start_time = datetime.now()

# Scan ports in the given range
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Timeout after 1 second
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is open")
    s.close()

end_time = datetime.now()
total_time = end_time - start_time
print(f"\nScan completed in: {total_time}")
