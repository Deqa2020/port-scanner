# 🔍 Port Scanner

A simple and effective Python-based port scanner designed to identify open ports on a given IP address or domain. This tool is essential for network reconnaissance and penetration testing tasks, allowing users to scan a range of ports to detect open services.

---

## 🧰 Features

- 🔎 **Scan Ports**: Scan a specified range of ports on any IP or domain.
- ⚡ **Real-Time Results**: Displays open ports as they’re found.
- 🛠️ **Built-in Libraries**: Uses Python’s `socket` library — no external dependencies.
- 🪶 **Lightweight**: Simple design for fast usage.
- ⏱️ **Time Tracking**: Displays how long the scan takes.

---

## 📦 Requirements

- ✅ **Python 3.x** — [Download here](https://www.python.org/downloads/)
- ✅ **Visual Studio Code (VS Code)** — [Download here](https://code.visualstudio.com/Download)
- ✅ **Python Extension for VS Code** (by Microsoft)
- 🚫 No additional libraries needed

---


> 📌 **The simple Python script is located at the bottom of this README.**

> Copy that code into your **Visual Studio Code (VS Code)** editor and follow the instructions below to run it.



## ▶️ How to Run in Visual Studio Code (VS Code)

1. **Install Visual Studio Code**  
   Download and install Visual Studio Code from [here](https://code.visualstudio.com/Download).

2. **Install Python Extension in VS Code**  
   - Open VS Code  
   - Press `Ctrl + Shift + X`  
   - Search for `Python` and install the one by Microsoft

3. **Create the Script File**  
   - Open a new file in VS Code  
   - Copy the Python code from the bottom of this README  
   - Save the file as `port_scanner.py`

4. **Open the Terminal**  
   - Click on `Terminal → New Terminal`  
   - Or press `` Ctrl + ` `` (backtick)

5. **Navigate to the Script Directory**:
   ```bash
   cd path/to/your/script

  6 Run the Script:
  
      python port_scanner.py
7 Enter the Target Information:

    Enter target IP address or domain: 192.168.1.155
    Enter starting port: 20
    Enter ending port: 100

8 View the Results

The script will show which ports are open and how long the scan took.

🧪 Example Output

    Enter target IP address or domain: 192.168.1.155
    Enter starting port: 20
    Enter ending port: 100
    Starting scan on 192.168.1.155
    Scanning ports 20 to 100...

    [+] Port 22 is open
    [+] Port 80 is open

    Scan completed in: 0:00:01.234567
    

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
  

