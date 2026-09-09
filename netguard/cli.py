"""
NetGuard CLI
Entry point for the network security toolkit.
"""

import argparse
import sys


def build_parser():
    parser = argparse.ArgumentParser(
        prog="netguard",
        description="NetGuard - A Python network security toolkit"
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

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    print(f"[NetGuard] Command '{args.command}' recognized. Implementation coming soon.")


if __name__ == "__main__":
    main()
