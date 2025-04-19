
🔍 Port Scanner
A simple and effective Python-based Port Scanner for identifying open ports on a given IP address or domain. This tool is useful for basic network reconnaissance and penetration testing tasks.

🧰 Features
Scans a range of ports on a specified host

Displays open ports in real-time

Uses Python’s built-in socket library

Lightweight and easy to use

Tracks scan duration

📦 Requirements
Python 3.x installed on your system
Download Python

⚙️ Installation
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/Deqa2020/port-scanner.git
cd port-scanner
▶️ How to Run
Run the script using Python:

bash
Copy
Edit
python port_scanner.py
Then enter the following when prompted:

yaml
Copy
Edit
Enter target IP address or domain: 192.168.1.155
Enter starting port: 20
Enter ending port: 100
Tip: 192.168.1.155 is an example of a local IP address (e.g. your Mac). You can scan your own computer or a device on your local network.

🧪 Example Usage
PowerShell / VS Code Example
powershell
Copy
Edit
PS C:\Users\deqoa\Downloads\port-scanner> & 'c:\Users\deqoa\AppData\Local\Microsoft\WindowsApps\python3.11.exe' 'c:\Users\deqoa\.vscode\extensions\ms-python.debugpy-2025.6.0-win32-x64\bundled\libs\debugpy\launcher' '56573' '--' 'c:\Users\deqoa\Downloads\port-scanner\port_scanner.py'
Input
yaml
Copy
Edit
Enter target IP address or domain: 192.168.1.155
Enter starting port: 20
Enter ending port: 100
Example Output
pgsql
Copy
Edit
Starting scan on 192.168.1.155
Scanning ports 20 to 100...

[+] Port 22 is open
[+] Port 80 is open

Scan completed in: 0:00:01.234567
🖼️ Screenshot
Here’s how it looks when running in the terminal:



🛠️ Troubleshooting

Issue	Solution
No output	No services running on those ports; try another target or port range
Python not found	Install Python or check PATH variable
Ports always closed	Check if the firewall is blocking connections or ports are just closed
⚠️ Disclaimer
This tool is intended for educational purposes only.
Do not use it to scan networks or devices you do not own or have permission to scan.

👤 Author
Deqa Mohamed








