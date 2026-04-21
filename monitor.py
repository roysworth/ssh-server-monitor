print("Script started")
import paramiko
import os
import sys
from io import StringIO

def main():
    host = os.environ.get("VM_IP")
    username = os.environ.get("VM_USER")
    private_key_str = os.environ.get("VM_SSH_KEY")

    if not all([host, username, private_key_str]):
        print("Missing environment variables. Set VM_IP, VM_USER, VM_SSH_KEY")
        sys.exit(1)

    try:
        private_key = paramiko.RSAKey.from_private_key(StringIO(private_key_str))
    except Exception as e:
        print(f"Invalid private key: {e}")
        sys.exit(1)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"Connecting to {host} as {username}...")
        client.connect(hostname=host, username=username, pkey=private_key)

        commands = [
            ("Uptime", "uptime -p"),
            ("CPU Load", "top -bn1 | grep 'load average'"),
            ("Memory", "free -h"),
            ("Disk /", "df -h /")
        ]

        print("\n--- Server Health Report ---\n")
        for title, cmd in commands:
            stdin, stdout, stderr = client.exec_command(cmd)
            output = stdout.read().decode().strip()
            print(f"{title}:\n{output}\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()