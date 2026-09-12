"""
NetGuard - Configuration Module
Loads user-defined defaults from a netguard.cfg file, falling back to
sensible built-in defaults if the file is missing or incomplete.
"""

import configparser
import os


DEFAULT_CONFIG = {
    "scan": {
        "default_ports": "1-1024",
        "max_workers": "100",
        "timeout": "0.5",
    },
    "discover": {
        "max_workers": "50",
        "timeout_ms": "1000",
    },
    "banner": {
        "timeout": "2.0",
    },
    "sniff": {
        "default_count": "20",
    },
}

CONFIG_FILENAME = "netguard.cfg"


def load_config(path: str = CONFIG_FILENAME) -> configparser.ConfigParser:
    """
    Load config from a .cfg file if present, layered on top of built-in
    defaults so missing sections/keys always fall back safely.
    """
    parser = configparser.ConfigParser()
    parser.read_dict(DEFAULT_CONFIG)

    if os.path.exists(path):
        parser.read(path)

    return parser


def generate_default_config_file(path: str = CONFIG_FILENAME):
    """
    Write out a netguard.cfg file populated with the default values,
    so users have a starting point to customize.
    """
    parser = configparser.ConfigParser()
    parser.read_dict(DEFAULT_CONFIG)
    with open(path, "w", encoding="utf-8") as f:
        parser.write(f)
    print(f"[*] Default config written to {path}")
