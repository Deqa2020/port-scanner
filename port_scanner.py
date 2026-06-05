# ----------------------------------------
# Port Scanner Script
# Author: Deqa Mohamed
# GitHub: https://github.com/Deqa2020
# LinkedIn: https://www.linkedin.com/in/deqa-mohamed-13149a23b/
# Description: Simple Python script to scan open ports on a host
# ----------------------------------------

import socket
from datetime import datetime

# Set timeout ONCE (important fix)
socket.setdefaulttimeout(1)

# Get user input
target = input("Enter target IP address or domain: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

# Header output (Nmap-style)
print(f"\nScanning target: {target}")
print(f"Ports: {start_port}-{end_port}")
print("-" * 40)
print(f"{'PORT':<10}{'STATE'}")
print("-" * 40)

start_time = datetime.now()

# Scan ports
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"{port}/tcp{'':<5}open")

    s.close()

end_time = datetime.now()
total_time = end_time - start_time

# Footer output
print("-" * 40)
print(f"Scan completed in: {total_time}")
