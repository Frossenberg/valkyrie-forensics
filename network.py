import whois
import dns.resolver
from colorama import Fore, Style

def network_recon(domain):
    print(f"{Fore.BLUE}[ANALYSIS]{Style.RESET_ALL} Starting Network Recon for: {domain}")
    
    # WHOIS Lookup
    try:
        print(f"{Fore.BLUE}[ANALYSIS]{Style.RESET_ALL} Performing WHOIS lookup...")
        w = whois.whois(domain)
        print(f"{Fore.GREEN}[EVIDENCE]{Style.RESET_ALL} WHOIS Data Received:")
        print(f"  Registrar: {w.registrar}")
        print(f"  Creation Date: {w.creation_date}")
        print(f"  Expiration Date: {w.expiration_date}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} WHOIS lookup failed: {e}")

    # DNS Enumeration
    try:
        print(f"{Fore.BLUE}[ANALYSIS]{Style.RESET_ALL} Performing DNS Enumeration...")
        record_types = ['A', 'MX', 'NS', 'TXT']
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                print(f"{Fore.GREEN}[EVIDENCE]{Style.RESET_ALL} {record} Records:")
                for rdata in answers:
                    print(f"  {rdata.to_text()}")
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                continue
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} DNS enumeration failed: {e}")
