import socket
from datetime import datetime

print("=" * 50)
print("         SecurePortScanner")
print("=" * 50)

host = input("Enter website or IP address to scan: ")

try:
    target_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Invalid website or IP address")
    exit()

print(f"\nScanning Target: {host}")
print(f"IP Address: {target_ip}")
print(f"Started at: {datetime.now()}")
print("-" * 50)

ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 8080]

for port in ports:
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target_ip, port))

    if result == 0:
        print(f"[OPEN] Port {port}")

    scanner.close()

print("-" * 50)
print("Scan Completed")
