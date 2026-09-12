# Changelog

All notable changes to this project are documented here.

## [Unreleased]
### Added
- Initial project structure
- CLI entry point placeholder
- Argparse-based CLI with subcommands (discover, scan, banner, arp, sniff)
- --version flag
- Multithreaded ping sweep for host discovery
- Discover command wired into CLI
- Multithreaded TCP port scanner with service name mapping
- Scan command wired into CLI
- Banner grabbing for service fingerprinting
- Banner command wired into CLI
- ARP scanner for local network device discovery (MAC addresses)
- ARP command wired into CLI
- Packet sniffer with per-packet protocol summaries
- Sniff command wired into CLI (with --count option)
- Input validation module for IPs, subnets, and ports
- Graceful error handling across all CLI commands (no more raw tracebacks)
- JSON and HTML report generator
- --output/--format flags for discover, scan, banner, and arp commands
- Unit test suite (pytest) for validators and port range parsing
- Logging module with daily rotating file logs and console warnings
- Logging integrated into all CLI commands for audit trail
- Config file support (netguard.cfg) with --init-config flag
- Scan and sniff commands now read defaults from config
- pyproject.toml for pip-installable packaging with netguard console command
- CONTRIBUTING.md with setup and contribution guidelines

### Changed
- README overhauled with full usage guide for all 5 core features
- README setup section documents pip install path
- LICENSE finalized with correct copyright holder

### Removed
- Unused early draft scaffolding (netguard/scanners, netguard/utils)
