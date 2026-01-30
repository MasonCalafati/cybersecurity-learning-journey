import os
import platform
import subprocess
from datetime import datetime

def ping_host(ip):
	"""Ping a single host and return True if alive"""
	param = '-n' if platform.system().lower() == 'windows' else '-c'
	command = ['ping', param, '1', ip]

	try:
		output = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		return output.returncode == 0
	except:
		return False

print("=" * 60)
print("         NETWORK PING SCANNER")
print("=" * 60)

network = input("\nEnter network (e.g., 192.168.1): ")
start = int(input("Start host number (e.g., 1): "))
end = int(input("End host number (e.g., 254): "))

print(f"\n[*] Scanning {network}.{start} to {network}.{end}")
start_time = datetime.now()
print(f"[*] Scan started: {datetime.now()}\n")
print("=" * 60)

alive_hosts = []
dead_hosts = []

for host in range(start, end + 1):
	ip = f"{network}.{host}"
	print(f"[*] Pinging {ip}...", end=" ")

	if ping_host(ip):
		print("✓ ALIVE")
		alive_hosts.append(ip)
	else:
		print("✗ Down")
		dead_hosts.append(ip)

print("\n" + "=" * 60)
print("         SCAN RESULTS")
print("=" * 60)

print(f"\n[+] Alive hosts: {len(alive_hosts)}")
for ip in alive_hosts:
    print(f"    - {ip}")

print(f"\n[-] Dead hosts: {len(dead_hosts)}")

end_time = datetime.now()
duration = end_time - start_time
print(f"\n[*] Scan completed: {end_time}")
print(f"[*] Duration: {duration}")
print("=" * 60)
