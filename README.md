# NetGuard 🛡️

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python-based network security toolkit for host discovery, port scanning,
banner grabbing, ARP scanning, and packet sniffing — built as part of my
Cybersecurity elective coursework.

## Status
🚧 In active development. See [CHANGELOG.md](CHANGELOG.md) for progress.

## Features
- [x] Host discovery (multithreaded ping sweep)
- [x] TCP port scanner (multithreaded, with service name mapping)
- [ ] Banner grabbing
- [ ] ARP scanner
- [ ] Packet sniffer
- [ ] HTML/JSON report generation

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/netguard.git
cd netguard
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run commands as a module from the project root:

```bash
python -m netguard.cli --help
```

### Host Discovery
Sweep a subnet for live hosts:
```bash
python -m netguard.cli discover 192.168.0.0/24
```

### Port Scanning
Scan a target host for open TCP ports:
```bash
python -m netguard.cli scan 192.168.0.1 -p 1-1024
python -m netguard.cli scan 192.168.0.1 -p 80,443,8080
```

## ⚠️ Legal Notice
Only use NetGuard against hosts and networks you own or have explicit
permission to test. Unauthorized scanning of devices you don't control
may be illegal in your jurisdiction.

## Project Structure
```
netguard/
├── netguard/
│   ├── __init__.py
│   ├── cli.py          # CLI entry point (argparse)
│   ├── discovery.py     # Host discovery (ping sweep)
│   └── scanner.py       # TCP port scanner
├── CHANGELOG.md
├── README.md
└── .editorconfig
```
