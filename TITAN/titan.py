#!/usr/bin/env python3
import argparse
import signal
import sys

from rich import print
from rich.console import Console

from tools.extract_ip import extract_ip
from tools.scan_paths import scan_paths
from tools.status_code import status_code

console = Console()

BANNER = "[bold green]TITAN[/bold green]\n\n[bold magenta]IMAD CAME TO UU[/bold magenta]\n"

USAGE_HELP = """
[bold yellow].................................: this tool made to scan for paths and to know ip and if the site is up or down[/bold yellow]

[bold green]Usage examples:[/bold green]
  [bold green]python3 titan.py ip[/bold green]
    [bold yellow]..............................-> show IP of the target site (follow prompts or as implemented in your extract_ip tool)[/bold yellow]

  [bold green]python3 titan.py paths -u[/bold green] [blue]http://example.com[/blue] [bold green]-w /home/kali/wordlists.txt -t 20[/bold green]
    [bold yellow]..............................-> scan paths from the provided wordlist against the given URL using N threads[/bold yellow]

  [bold green]python3 titan.py code[/bold green]
    [bold yellow]..............................-> check if the site is up (status code related tool)[/bold yellow]
"""

def sigint_handler(signum, frame):
    print("\n[red][!] Interrupted by user (SIGINT). Exiting...[/red]")
    sys.exit(0)

def print_banner_and_help():
    console.print(BANNER, justify="center")
    console.print(USAGE_HELP)

def main():
    print_banner_and_help()

    preser = argparse.ArgumentParser(
        description='IP SCAN / PATHS SCAN / STATUS CODE',
        add_help=True
    )
    preser.add_argument('command', choices=['ip', 'paths', 'code'], help='command tools run')
    args, unknown = preser.parse_known_args()

    if args.command == 'ip':
        extract_ip()
    elif args.command == 'paths':
        scan_paths()
    elif args.command == 'code':
        status_code()
    else:
        preser.print_help()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    try:
        main()
    except KeyboardInterrupt:
        print("\n[red][!] Interrupted by user. Exiting...[/red]")
        sys.exit(0)
