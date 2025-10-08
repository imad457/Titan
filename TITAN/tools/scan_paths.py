import argparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin
import requests
from rich import print

TIMEOUT = 5
HEADERS = {"User-Agent": "scan_paths/1.0"}

def scan_paths():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--url","-u", required=True, help="Target URL (https://example.com)")
    parser.add_argument('--wordlist',"-w", required=True, help="Path to wordlist txt")
    parser.add_argument("--threads", "-t", type=int, default=20, help="Number of threads")
    known_args, _ = parser.parse_known_args()

    base = known_args.url.strip()
    if not base.startswith(("http://", "https://")):
        base = "http://" + base
    base = base.rstrip("/")

    wl_path = known_args.wordlist
    if not os.path.isfile(wl_path):
        print(f"[red]Wordlist not found:[/] {wl_path}")
        return

    with open(wl_path, "r", encoding="utf-8", errors="ignore") as f:
        words = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    if not words:
        print("[yellow]Wordlist empty[/yellow]")
        return

    def _check(path):
        p = path.lstrip("/")
        full = urljoin(base + "/", p)
        try:
            r = requests.head(full, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
            status = r.status_code
            if status == 405:
                r = requests.get(full, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
                status = r.status_code
            return full, status
        except requests.exceptions.RequestException:
            return full, None

    def _print(full, status):
        if isinstance(status, int):
            if status == 200:
                print(f"[bold green][{status}][/bold green] {full}")
            elif status == 301:
                print(f"[bold yellow][{status}][/bold yellow] {full}")
            elif 400 <= status < 600:
                print(f"[bold red][{status}][/bold red] {full}")
            else:
                print(f"[white][{status}][/white] {full}")
        else:
            print(f"[bold red]ERR[/bold red] {full}")

    threads = known_args.threads if known_args.threads and known_args.threads > 0 else 10
    with ThreadPoolExecutor(max_workers=threads) as ex:
        futures = {ex.submit(_check, w): w for w in words}
        for fut in as_completed(futures):
            full, status = fut.result()
            _print(full, status)
