# Network Monitoring Tools

Collection of network analysis tools for monitoring connections and scanning for security issues.

## Tools Included

### 1. Packet Analyzer (network_monitor.py)
Analyzes network packet structure and identifies protocols.

**Features:**
- Parses Ethernet, IPv4, and TCP packet headers
- Identifies network protocols
- Flags suspicious remote access ports (SSH, Telnet, RDP)

### 2. Connection Scanner (connection_monitor.py)
Scans networks for open ports and identifies running services.

**Features:**
- Scans common security-relevant ports
- Identifies services (HTTP, SSH, FTP, MySQL, RDP, etc.)
- Alerts on potentially risky open ports
- Local and remote network scanning

## Technical Skills Demonstrated
- Network protocol analysis
- Socket programming in Python
- Binary data parsing (struct module)
- Security monitoring concepts
- Service enumeration

## Usage

**Connection Scanner:**
```bash
python3 connection_monitor.py
```
Enter target IP or press Enter for localhost scan.

**Packet Analyzer:**
```bash
sudo python3 network_monitor.py
```
Note: Requires administrator/root privileges for packet capture.

## Demo
![Network Monitor Demo](https://github.com/MasonCalafati/cybersecurity-learning-journey/blob/main/network-monitor/connection%20monitor.png?raw=true)
