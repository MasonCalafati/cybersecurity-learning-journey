import socket
from datetime import datetime

# Common port services
PORT_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

def scan_port(target_ip, port):
    """Scan a single port and return if it's open"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        s.close()
        return result == 0
    except:
        return False

# Main program
print("=" * 50)
print("         SIMPLE PORT SCANNER")
print("=" * 50)

target = input("\nEnter target IP or hostname: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved")
    exit()

print(f"\nTarget IP: {target_ip}")
print(f"Scan started: {datetime.now()}")
print("-" * 50)

# Ask if user wants to scan custom range
custom = input("\nScan custom port range? (y/n): ")

open_ports = []

if custom.lower() == 'y':
    try:
        start = int(input("Start port: "))
        end = int(input("End port: "))
        
        print(f"\nScanning ports {start}-{end}...")
        
        for port in range(start, end + 1):
            if scan_port(target_ip, port):
                service = PORT_SERVICES.get(port, "Unknown")
                print(f"Port {port}: OPEN - {service}")
                open_ports.append(port)
    except ValueError:
        print("Invalid port range")

# Scan common ports
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]

print("\nScanning common ports...")

for port in common_ports:
    if scan_port(target_ip, port):
        service = PORT_SERVICES.get(port, "Unknown")
        print(f"Port {port}: OPEN - {service}")
        if port not in open_ports:
            open_ports.append(port)

print("\n" + "-" * 50)
print(f"Scan completed: {datetime.now()}")
print(f"\nTotal open ports found: {len(open_ports)}")
if open_ports:
    print(f"Open ports: {open_ports}")
else:
    print("No open ports found")
print("=" * 50)
