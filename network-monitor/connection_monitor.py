import socket
from datetime import datetime

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "Unable to determine"

def scan_common_ports(host):
    common_ports = {
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
        5900: "VNC",
        8080: "HTTP-Alt"
    }
    
    open_ports = []
    
    print(f"Scanning {host}...\n")
    
    for port, service in common_ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append((port, service))
                print(f"[+] Port {port} ({service}): OPEN")
            sock.close()
        except:
            pass
    
    return open_ports

def main():
    print("=" * 60)
    print("         LOCAL NETWORK MONITOR")
    print("=" * 60)
    print(f"\nScan Time: {datetime.now()}\n")
    
    local_ip = get_local_ip()
    hostname = socket.gethostname()
    
    print(f"Hostname: {hostname}")
    print(f"Local IP: {local_ip}")
    print("-" * 60)
    
    target = input("\nEnter IP to scan (or press Enter for localhost): ")
    
    if not target:
        target = "127.0.0.1"
        print(f"\nScanning localhost (127.0.0.1)...")
    
    print("\n" + "=" * 60)
    open_ports = scan_common_ports(target)
    
    print("\n" + "=" * 60)
    print("         SCAN RESULTS")
    print("=" * 60)
    
    if open_ports:
        print(f"\n[!] Found {len(open_ports)} open ports:\n")
        for port, service in open_ports:
            status = "[!] ALERT" if port in [22, 23, 3389, 5900] else "[*]"
            print(f"{status} Port {port} - {service}")
            
        suspicious = [p for p, s in open_ports if p in [22, 23, 3389, 5900]]
        if suspicious:
            print(f"\n[!] WARNING: {len(suspicious)} potentially risky ports open")
    else:
        print("\n[+] No open ports found")
    
    print("\n" + "=" * 60)
    print(f"Scan completed: {datetime.now()}")
    print("=" * 60)

if __name__ == '__main__':
    main()
