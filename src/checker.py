import requests
import socket
from datetime import datetime

INPUT_FILE = "subdomains.txt"
OUTPUT_FILE = "takeover_targets.txt"

ERROR_SIGNATURES = [
    "nxdomain",
    "nosuchbucket"
]


def check_subdomain(subdomain):
    subdomain = subdomain.strip()

    if not subdomain:
        return None

    print(f"\n[+] Checking: {subdomain}")

    # DNS Analysis
    try:
        ip_address = socket.gethostbyname(subdomain)
        dns_status = f"Resolved: {ip_address}"

        print(f"[DNS] {dns_status}")

    except socket.gaierror:
        dns_status = "DNS resolution failed"

        print(f"[DNS] {dns_status}")

        return {
            "subdomain": subdomain,
            "dns": dns_status,
            "http": "Not checked",
            "signature": "None"
        }

    # HTTP Analysis
    try:
        response = requests.get(
            f"https://{subdomain}",
            timeout=5,
            allow_redirects=True
        )

        content = response.text.lower()

        print(f"[HTTP] Status: {response.status_code}")

        for signature in ERROR_SIGNATURES:
            if signature in content:

                print(
                    f"[!] Potential indicator: {signature}"
                )

                return {
                    "subdomain": subdomain,
                    "dns": dns_status,
                    "http": str(response.status_code),
                    "signature": signature
                }

        print("[OK] No matching signature")

        return {
            "subdomain": subdomain,
            "dns": dns_status,
            "http": str(response.status_code),
            "signature": "None"
        }

    except requests.RequestException as error:

        print(f"[ERROR] {error}")

        return {
            "subdomain": subdomain,
            "dns": dns_status,
            "http": "Request failed",
            "signature": "None"
        }


def main():

    findings = []

    with open(INPUT_FILE, "r") as file:
        subdomains = file.readlines()

    for subdomain in subdomains:

        result = check_subdomain(subdomain)

        if result:
            findings.append(result)

    with open(OUTPUT_FILE, "w") as file:

        file.write("Subdomain Takeover Checker Report\n")
        file.write(f"Generated: {datetime.now()}\n")
        file.write("=" * 50 + "\n\n")

        for finding in findings:

            file.write(
                f"Subdomain: {finding['subdomain']}\n"
            )

            file.write(
                f"DNS: {finding['dns']}\n"
            )

            file.write(
                f"HTTP: {finding['http']}\n"
            )

            file.write(
                f"Signature: {finding['signature']}\n"
            )

            file.write("-" * 50 + "\n")

    print("\n[+] Scan completed!")
    print(f"[+] Results saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()