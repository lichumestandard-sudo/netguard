"""
NetGuard - Banner Grabbing Module
Connects to an open TCP port and attempts to read the service banner.
"""

import socket


def grab_banner(target: str, port: int, timeout: float = 2.0) -> str:
    """
    Connect to a target:port and attempt to read a banner.
    Some services announce themselves immediately (SSH, FTP, SMTP).
    Others (like HTTP) require a request before responding.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((target, port))

            # HTTP-like ports need a request sent first
            if port in (80, 8080, 8000):
                request = f"HEAD / HTTP/1.1\r\nHost: {target}\r\nConnection: close\r\n\r\n"
                sock.sendall(request.encode())

            banner = sock.recv(1024)
            decoded = banner.decode(errors="replace").strip()
            return decoded if decoded else "(no banner received)"

    except socket.timeout:
        return "(connection timed out — port may be open but silent)"
    except ConnectionRefusedError:
        return "(connection refused — port likely closed)"
    except socket.error as e:
        return f"(error: {e})"


def grab_banners(target: str, ports: list, timeout: float = 2.0) -> dict:
    """
    Grab banners from multiple ports on a target. Returns {port: banner}.
    """
    results = {}
    for port in ports:
        print(f"[*] Grabbing banner from {target}:{port}...")
        banner = grab_banner(target, port, timeout)
        results[port] = banner
        print(f"[+] {port}: {banner}\n")
    return results
