# SSH Server Monitor

A Python script that connects to a remote Linux server over SSH and reports system health: uptime, CPU load, memory usage, and disk space.

## Features
- Secure SSH connection using key-based authentication
- Executes remote commands to gather system statistics
- Displays a clean, formatted health report
- Uses environment variables for credentials (no hardcoded secrets)

## Technologies Used
- Python 3
- Paramiko (SSH library)
- Google Cloud Compute Engine (free tier)

## Prerequisites
- A remote Linux server with SSH enabled
- Python 3.6+ installed locally

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/roysworth/ssh-server-monitor.git
   cd ssh-server-monitor

2. **Create and activate a virtual environment**

bash
python -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Set environment variables (PowerShell example)

powershell
$env:VM_IP = "your.server.ip"
$env:VM_USER = "your_username"
$env:VM_SSH_KEY = @"
-----BEGIN OPENSSH PRIVATE KEY-----
...your private key...
-----END OPENSSH PRIVATE KEY-----
"@

3. **Install dependencies**

bash
pip install -r requirements.txt

4. **Set environment variables (PowerShell example)**

powershell
$env:VM_IP = "your.server.ip"
$env:VM_USER = "your_username"
$env:VM_SSH_KEY = @"
-----BEGIN OPENSSH PRIVATE KEY-----
...your private key...
-----END OPENSSH PRIVATE KEY-----
"@

5. Run the monitor

bash
python monitor.py

Connecting to 8.230.114.131 as roysworth...

--- Server Health Report ---

Uptime: up 1 hour, 2 minutes
CPU Load: load average: 0.00, 0.01, 0.00
Memory: total 3.8Gi, used 532Mi, free 2.4Gi
Disk /: 29G size, 2.5G used, 26G available
