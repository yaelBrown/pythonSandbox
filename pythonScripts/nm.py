#!/usr/bin/env python3

"""
Used to automate ping and nmap for pentests
"""

import os
import argparse

def _msg(message, sentiment=1):
    """Prints messages with different sentiment markers"""
    if sentiment == 2:
        print(f"[+] {message}")
    elif sentiment == 0:
        print(f"[-] {message}")
    else:
        print(f"[ ] {message}")

def ping_target(targ):
    _msg("Pinging target", 1) 
    os.system(f"ping -c 1 {targ}")

def nmap_target(name, targ):
    os.system(f"sudo nmap -sC -sV -vv -oA {name} {targ}")

def app(name, targ):
    ping_target(targ)
    nmap_target(name, targ)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate ping & Nmap scanning.")
    
    parser.add_argument("-u", "--host", help="Target Host IP", type=str, required=True)
    parser.add_argument("-n", "--name", help="Name of the target (or VM box)", type=str, required=True)

    args = parser.parse_args()

    app(args.name, args.host)
