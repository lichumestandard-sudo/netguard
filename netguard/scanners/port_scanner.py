import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """Attempts to connect to a specific port on the target IP."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0) # 1 second timeout
        result = sock.connect_ex((ip, port))
        sock.close()
        
        if result == 0:
            return port, True
        return port, False
    except Exception:
        return port, False

def parse_ports(port_string):
    """Converts strings like '22,80,443' or '1-100' into a list of integers."""
    ports = []
    for part in port_string.split(','):
        if '-' in part:
            start, end = part.split('-')
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))
    return ports

def run_port_scan(target, port_string):
    print(f"[*] Starting TCP port scan on {target}...")
    ports = parse_ports(port_string)
    open_ports = []
    
    # ThreadPoolExecutor speeds up scanning by checking multiple ports at once
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(target, p), ports)
        
        for port, is_open in results:
            if is_open:
                print(f"[+] Port {port}/tcp is OPEN")
                open_ports.append(port)
                
    if not open_ports:
        print("[-] No open ports found.")
    else:
        print(f"[*] Scan complete. Found {len(open_ports)} open ports.")