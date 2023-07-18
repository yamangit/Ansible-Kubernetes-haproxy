import subprocess
import sys
import os
import getpass

def ssh_copy_id(username, host, password, port=22):
    try:
        subprocess.run(["sshpass", "-p", password, "ssh-copy-id", "-o", "StrictHostKeyChecking=no", "-p", str(port), f"{username}@{host}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    username = input("Enter your SSH username: ")

    password = getpass.getpass("Enter your SSH password: ")

    if not username or not password:
        print("Username and password cannot be empty.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python copy_sshkey.py path_to_host_file")
        sys.exit(1)

    host_file_path = sys.argv[1]

    with open(host_file_path, "r") as host_file:
        for line in host_file:
            host = line.strip()
            ssh_copy_id(username, host, password)