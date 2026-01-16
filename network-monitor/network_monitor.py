import socket
import struct

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

def get_ip(addr):
    return '.'.join(map(str, addr))

def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, get_ip(src), get_ip(target), data[header_length:]

def tcp_segment(data):
    (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

def main():
    print("=" * 60)
    print("         NETWORK TRAFFIC MONITOR")
    print("=" * 60)
    print("\nMonitoring network traffic...")
    print("Press Ctrl+C to stop\n")
    print("-" * 60)
    
    try:
        conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    except:
        print("[!] ERROR: This requires administrator/root privileges")
        print("[!] On Windows: Run as Administrator")
        print("[!] On Linux: Run with sudo")
        return
    
    packet_count = 0
    
    try:
        while True:
            raw_data, addr = conn.recvfrom(65536)
            packet_count += 1
            
            dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
            
            print(f'\n[Packet #{packet_count}]')
            print(f'Ethernet Frame:')
            print(f'  Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}')
            
            if eth_proto == 8:
                (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
                print(f'IPv4 Packet:')
                print(f'  Version: {version}, Header Length: {header_length}, TTL: {ttl}')
                print(f'  Protocol: {proto}, Source: {src}, Target: {target}')
                
                if proto == 6:
                    src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = tcp_segment(data)
                    print(f'TCP Segment:')
                    print(f'  Source Port: {src_port}, Destination Port: {dest_port}')
                    print(f'  Sequence: {sequence}, Acknowledgment: {acknowledgment}')
                    print(f'  Flags:')
                    print(f'    URG: {flag_urg}, ACK: {flag_ack}, PSH: {flag_psh}')
                    print(f'    RST: {flag_rst}, SYN: {flag_syn}, FIN: {flag_fin}')
                    
                    if src_port in [22, 23, 3389] or dest_port in [22, 23, 3389]:
                        print(f'  [!] ALERT: Remote access port detected ({src_port}/{dest_port})')
            
            print("-" * 60)
            
    except KeyboardInterrupt:
        print(f'\n\n[*] Monitoring stopped')
        print(f'[*] Total packets captured: {packet_count}')
        print("=" * 60)

if __name__ == '__main__':
    main()
