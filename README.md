# 🔍 Port Scanner (Python)

A lightweight TCP port scanning tool used to identify open ports and exposed services on a target system. This project demonstrates foundational concepts in vulnerability assessment, network reconnaissance, and attack surface identification.

---

## 🎯 Security Purpose

Open ports represent potential entry points for attackers. This tool helps security analysts identify:

- Exposed network services  
- Unnecessary open ports  
- Potential attack surface risks  
- Misconfigured systems  

This aligns with early-stage vulnerability assessment and SOC workflows.

---

## ⚙️ Features

- TCP port scanning across a defined range  
- Real-time detection of open ports  
- Lightweight implementation using Python standard libraries  
- Execution time tracking for performance analysis  

---

## 🧪 Example Output

🧪 Example Output

Enter target IP address or domain: 192.168.1.155
Enter starting port: 20
Enter ending port: 100

Starting scan on 192.168.1.155
Scanning ports 20 to 100...

[+] Port 22 is open
[+] Port 80 is open

Scan completed in: 0:00:01.234567


---

## 🔍 How It Works

- Uses Python `socket` library to attempt TCP connections  
- Iterates through a user-defined port range  
- If connection succeeds → port is OPEN  
- If connection fails → port is CLOSED/FILTERED  

---

## ⚠️ Legal Disclaimer

This tool is intended for educational and authorized security testing only.

Unauthorized scanning of systems or networks is illegal and unethical.

---

## 🛠️ Technical Stack

- Python 3.x  
- socket (standard library)  
- datetime module  

---

## 👨‍💻 Author

Deqa Mohamed  
Cybersecurity Student | SOC & Vulnerability Analyst Track
