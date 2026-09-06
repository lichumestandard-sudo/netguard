import argparse
import sys

def main():
parser = argparse.ArgumentParser(
    description="NetGuard 🛡️ - Network Security Toolkit",
    formatter_class=argparse.RawTextHelpFormatter
)

parser.add_argument("-v", "--version", action="version", version="NetGuard v0.1")

# Subparsers for different modules
subparsers = parser.add_subparsers(dest="command", help="Available modules")

# Port Scanner parser
scan_parser = subparsers.add_parser("scan", help="Run TCP port scanner")
scan_parser.add_argument("-t", "--target", help="Target IP", required=True)
scan_parser.add_argument("-p", "--ports", help="Ports to scan (e.g., 22,80,443)", default="1-1000")

# ARP Scanner parser
arp_parser = subparsers.add_parser("arp", help="Run ARP discovery scan")
arp_parser.add_argument("-t", "--target", help="Target subnet (e.g., 192.168.1.0/24)", required=True)

args = parser.parse_args()

if not args.command:
    parser.print_help()
    sys.exit(1)
    
print(f"[*] Initializing {args.command} module against {args.target}...")

if __name__ == "__main__":
main()
