import os
import re
import sys
import urllib.request
import urllib.error

def main():
    owner = os.getenv("GITHUB_REPOSITORY_OWNER", "space-timed")
    repo = os.getenv("GITHUB_REPOSITORY", f"{owner}/{owner}")

    urls_to_scan = [
        f"https://github.com/{owner}",
        f"https://github.com/{repo}",
    ]

    camo_urls = set()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    print(f"Scanning pages for Camo URLs for {owner} ({repo})...")
    for page in urls_to_scan:
        try:
            req = urllib.request.Request(page, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
                matches = re.findall(r"https://camo\.githubusercontent\.com/[a-zA-Z0-9/_?=:-]+", html)
                camo_urls.update(matches)
                print(f"Found {len(matches)} Camo references on {page}")
        except Exception as e:
            print(f"Warning: could not scan {page}: {e}")

    if not camo_urls:
        print("No Camo URLs found.")
        return

    print(f"\nPurging cache for {len(camo_urls)} unique Camo URLs:")
    for url in sorted(camo_urls):
        print(f"Purging: {url}")
        try:
            req = urllib.request.Request(url, method="PURGE", headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"  -> Status: {resp.status} ({resp.read().decode('utf-8', errors='ignore').strip()})")
        except urllib.error.HTTPError as e:
            print(f"  -> HTTP Error {e.code}: {e.reason}")
        except Exception as e:
            print(f"  -> Error: {e}")

    print("\nCamo cache purge completed successfully.")

if __name__ == "__main__":
    main()
