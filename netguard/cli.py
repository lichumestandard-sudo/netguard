"""
NetGuard CLI
Entry point for the network security toolkit.
"""

import argparse
import sys

from netguard.discovery import discover_hosts
from netguard.scanner import scan_ports
from netguard.banner import grab_banner
from netguard.arp_scan import arp_scan
from netguard.sniffer import start_sniffer


def build_parser():
    parser = argparse.ArgumentParser(
        prog="netguard",
        description="NetGuard - A Python network security toolkit"
    )
    parser.add_argument(
        "-v", "--version", action="version", version="NetGuard 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # host discovery
    discover_parser = subparsers.add_parser("discover", help="Discover live hosts on a network")
    discover_parser.add_argument("target", help="Target subnet, e.g. 192.168.1.0/24")

    # port scan
    scan_parser = subparsers.add_parser("scan", help="Scan ports on a target host")
    scan_parser.add_argument("target", help="Target IP address")
    scan_parser.add_argument("-p", "--ports", default="1-1024", help="Port range, e.g. 1-1024")

    # banner grab
    banner_parser = subparsers.add_parser("banner", help="Grab service banners from open ports")
    banner_parser.add_argument("target", help="Target IP address")
    banner_parser.add_argument("port", type=int, help="Target port")

    # ARP scan
    arp_parser = subparsers.add_parser("arp", help="Perform an ARP scan on the local network")
    arp_parser.add_argument("target", help="Target subnet, e.g. 192.168.1.0/24")

    # packet sniffer
    sniff_parser = subparsers.add_parser("sniff", help="Sniff packets on a network interface")
    sniff_parser.add_argument("-i", "--interface", help="Network interface to sniff on")
    sniff_parser.add_argument("-c", "--count", type=int, default=20, help="Number of packets to capture")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "discover":
        live_hosts = discover_hosts(args.target)
        print(f"\n[*] Discovery complete. {len(live_hosts)} host(s) up.")

    elif args.command == "scan":
        open_ports = scan_ports(args.target, args.ports)
        print(f"\n[*] Scan complete. {len(open_ports)} open port(s) found.")

    elif args.command == "banner":
        result = grab_banner(args.target, args.port)
        print(f"[{args.target}:{args.port}] {result}")

    elif args.command == "arp":
        devices = arp_scan(args.target)
        print(f"\n[*] ARP scan complete. {len(devices)} device(s) found.")

    elif args.command == "sniff":
        start_sniffer(interface=args.interface, count=args.count)

    else:
        print(f"[NetGuard] Command '{args.command}' recognized. Implementation coming soon.")


if __name__ == "__main__":
    main()
