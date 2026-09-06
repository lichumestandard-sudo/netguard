# NetGuard 🛡️

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python-based network security toolkit for host discovery, port scanning,
banner grabbing, ARP scanning, and packet sniffing — built as part of my
Cybersecurity elective coursework.

## Status
🚧 In active development. See [CHANGELOG.md](CHANGELOG.md) for progress.

## Features (in progress)
- [ ] Host discovery (ping sweep)
- [ ] TCP port scanner
- [ ] Banner grabbing
- [ ] ARP scanner
- [ ] Packet sniffer
- [ ] HTML/JSON report generation

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/netguard.git
cd netguard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
NetGuard uses a modular command-line interface:
```bash
# View help
python netguard/cli.py --help

# Run a port scan
python netguard/cli.py scan -t 192.168.1.1 -p 22,80,443

# Run an ARP scan
python netguard/cli.py arp -t 192.168.1.0/24

## Usage
NetGuard uses a modular command-line interface:
```bash
# View help
python netguard/cli.py --help

# Run a port scan
python netguard/cli.py scan -t 192.168.1.1 -p 22,80,443

# Run an ARP scan
python netguard/cli.py arp -t 192.168.1.0/24
```
