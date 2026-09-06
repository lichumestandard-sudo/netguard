import argparse
import sys

def main():
parser = argparse.ArgumentParser(
    description="NetGuard 🛡️ - Network Security Toolkit",
    epilog="Example: python cli.py -t 192.168.1.1"
)

parser.add_argument("-t", "--target", help="Target IP address or subnet", required=False)
parser.add_argument("-v", "--version", action="version", version="NetGuard v0.1")

args = parser.parse_args()

if not args.target:
    parser.print_help()
    sys.exit(1)
    
print(f"[*] Target set to: {args.target}")

if __name__ == "__main__":
main()
