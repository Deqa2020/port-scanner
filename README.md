# 🔍 Port Scanner (Python)

A lightweight TCP port scanning tool used to identify open ports and exposed services on a target system. This project demonstrates foundational concepts in vulnerability assessment, network reconnaissance, and attack surface identification.

---

## 🎯 Security Purpose

Open ports represent potential entry points for attackers. This tool helps security analysts and students identify:

- Exposed network services
- Unnecessary open ports
- Potential attack surface risks
- Misconfigured systems

This aligns with early-stage vulnerability assessment and SOC analysis workflows.

---

## ⚙️ Features

- TCP port scanning across a defined range
- Real-time detection of open ports
- Lightweight implementation using Python standard libraries
- Execution time tracking for performance analysis

---

## 🧪 Example Output

Enter target IP address or domain: 192.168.1.155
Enter starting port: 20
Enter ending port: 100

Starting scan on 192.168.1.155
Scanning ports 20 to 100...

[+] Port 22 is open
[+] Port 80 is open

Scan completed in: 0:00:01.234567    





> 📌 **The simple Python script is located at the bottom of this README.**

> Copy that code into your **Visual Studio Code (VS Code)** editor and follow the instructions below to run it.



---

## 🔍 How It Works

- Uses Python `socket` library to attempt TCP connections
- Iterates through a user-defined port range
- If connection succeeds → port is OPEN
- If connection fails → port is CLOSED/FILTERED

---

## 📊 Security Relevance (IMPORTANT)

This tool demonstrates key cybersecurity concepts:

- Vulnerability identification
- Attack surface mapping
- Network exposure analysis
- Early-stage reconnaissance techniques

Used in security operations to support:
- Vulnerability assessments
- Risk identification
- Infrastructure security review

---

## ⚠️ Legal Disclaimer

This tool is intended for educational and authorized security testing only.

Scanning systems without permission is illegal and unethical.

---

## 🛠️ Technical Stack

- Python 3.x
- socket (standard library)
- datetime module

---

## 👨‍💻 Author

Deqa Mohamed  
Cybersecurity Student | SOC & Vulnerability Analyst Track
    

⚠️ Disclaimer

This tool is intended for educational purposes only. 


Do not scan devices or networks you do not own or have explicit permission to test.

✅ Always scan your own computer or network.

💡 To find your own IP address on Windows, open Command Prompt and run:

        ipconfig

## 🛠️ Troubleshooting

| **Issue**             | **Solution**                                                        |
|-----------------------|---------------------------------------------------------------------|
| **No output**         | No services are running on those ports — try a different target or range. |
| **Python not found**  | Install Python or check your system's PATH variable.                |
| **Ports always closed**| Check if firewall or antivirus is blocking connections.            |





## 📝 Port Scanner Python Code

```python
# ---------------------------------------- 
# Port Scanner Script
# Author: Deqa Mohamed
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
  

