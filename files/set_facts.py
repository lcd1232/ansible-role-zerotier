#!/usr/bin/env python3
import json
import os
import subprocess
import sys

FACTS_DIR = '/etc/ansible/facts.d'
FACT_FILE = os.path.join(FACTS_DIR, 'zerotier.fact')


def get_node_status():
    """Get node status using zerotier-cli with JSON output."""
    result = subprocess.run(
        ['zerotier-cli', '-j', 'status'],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error getting node status: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def get_networks():
    """Get networks using zerotier-cli with JSON output."""
    result = subprocess.run(
        ['zerotier-cli', '-j', 'listnetworks'],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error getting networks: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def build_facts():
    """Build the facts dictionary from zerotier-cli output."""
    status = get_node_status()
    networks_list = get_networks()

    networks = {}
    for network in networks_list:
        networks[network['nwid']] = {
            'status': network['status'],
            'device': network['portDeviceName']
        }

    return {
        'node_id': status['address'],
        'networks': networks
    }


def main():
    if not os.path.isdir(FACTS_DIR):
        os.makedirs(FACTS_DIR)

    facts = build_facts()

    with open(FACT_FILE, 'w') as f:
        json.dump(facts, f, indent=2)


if __name__ == '__main__':
    main()
