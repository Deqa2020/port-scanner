# 🔍 **Port Scanner**

A simple and effective **Python-based Port Scanner** designed to identify open ports on a given IP address or domain. This tool is essential for **network reconnaissance** and **penetration testing** tasks, allowing users to scan a range of ports to detect open services.

---

## 🧰 **Features**

- **Scan Ports**: Scans a specified range of ports on a target machine or domain.
- **Real-Time Results**: Displays which ports are open in real-time during the scan.
- **Socket Library**: Built using Python's built-in `socket` library, no external dependencies required.
- **Lightweight and Easy to Use**: Simple design and easy setup for anyone to use.
- **Track Duration**: Shows the time taken to complete the port scan.

---

## 📦 **Requirements**

- **Python 3.x** installed on your system (you can download it [here](https://www.python.org/downloads/)).
- No other dependencies are required, as the script uses Python's built-in `socket` library.

---

## ⚙️ **Installation**

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/Deqa2020/port-scanner.git
cd port-scanner


▶️ How to Run

Run the script using Python:

python port_scanner.py


You will be prompted to enter:

Enter target IP address or domain: 192.168.1.155
Enter starting port: 20
Enter ending port: 100


🧪 Example Usage

Here’s what it looks like when running the script:

Enter target IP address or domain: 192.168.1.155
Enter starting port: 20
Enter ending port: 100
Starting scan on 192.168.1.155
Scanning ports 20 to 100...

[+] Port 22 is open
[+] Port 80 is open

Scan completed in: 0:00:01.234567



🛠️ Troubleshooting


Issue                       | Solution
No output                   | No services running on those ports; try another target or port range.
Python not found            | Install Python or check PATH variable.
Ports always closed         | Check if the firewall is blocking connections or ports are just closed.



⚠️ Disclaimer
This tool is intended for educational purposes only. Do not use it to scan networks or devices that you do not own or do not have permission to scan.

✅ Always scan your own computer or network.

💡 To find your IP address on Windows, open Command Prompt and type:

ipconfig

Use the IP shown under IPv4 Address to scan your own machine.

For example: I used this tool to scan my HP laptop on my home network.

🔐 Unauthorized scanning can be illegal and may violate terms of service. Use responsibly.

## 📸 Port Scanning Demo

This screenshot shows the script in action:





