"""
NetGuard - Packet Sniffer Module
Captures live packets on a network interface and prints a summary of each.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP


def summarize_packet(packet) -> str:
    """
    Build a short human-readable summary line for a captured packet.
    """
    if IP not in packet:
        return f"[non-IP packet] {packet.summary()}"

    src = packet[IP].src
    dst = packet[IP].dst

    if TCP in packet:
        proto = "TCP"
        sport = packet[TCP].sport
        dport = packet[TCP].dport
        return f"{proto} {src}:{sport} -> {dst}:{dport}"
    elif UDP in packet:
        proto = "UDP"
        sport = packet[UDP].sport
        dport = packet[UDP].dport
        return f"{proto} {src}:{sport} -> {dst}:{dport}"
    elif ICMP in packet:
        return f"ICMP {src} -> {dst}"
    else:
        return f"IP {src} -> {dst} (other protocol)"


def start_sniffer(interface: str = None, count: int = 20):
    """
    Sniff a fixed number of packets on the given interface (or default
    interface if None) and print a summary of each as it's captured.
    """
    print(f"[*] Starting packet capture (interface={interface or 'default'}, count={count})...")
    print("[*] Press Ctrl+C to stop early.\n")

    def handle_packet(packet):
        print(f"[+] {summarize_packet(packet)}")

    try:
        sniff(iface=interface, prn=handle_packet, count=count, store=False)
    except PermissionError:
        raise PermissionError(
            "Packet sniffing requires elevated privileges. "
            "Try running your terminal as Administrator."
        )
    except OSError as e:
        raise OSError(
            f"Sniffing failed: {e}. "
            "Make sure Npcap is installed (https://npcap.com) and the "
            "interface name is correct."
        )

    print("\n[*] Capture complete.")
