"""
NetGuard - ARP Scanner Module
Discovers devices on the local network segment using ARP requests.
More reliable than ICMP ping sweeps for local subnets, and reveals MAC addresses.
"""

from scapy.all import ARP, Ether, srp


def arp_scan(subnet: str, timeout: int = 3) -> list:
    """
    Send ARP requests across a subnet (e.g. '192.168.0.0/24') and
    return a list of dicts: [{'ip': ..., 'mac': ...}, ...]
    """
    arp_request = ARP(pdst=subnet)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    print(f"[*] Sending ARP requests to {subnet}...")

    try:
        answered, _ = srp(packet, timeout=timeout, verbose=False)
    except PermissionError:
        raise PermissionError(
            "ARP scanning requires elevated privileges. "
            "Try running your terminal as Administrator."
        )
    except OSError as e:
        raise OSError(
            f"ARP scan failed: {e}. "
            "Make sure Npcap is installed (https://npcap.com)."
        )

    devices = []
    for sent, received in answered:
        device = {"ip": received.psrc, "mac": received.hwsrc}
        print(f"[+] {device['ip']} - {device['mac']}")
        devices.append(device)

    return devices
