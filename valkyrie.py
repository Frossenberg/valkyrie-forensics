import sys
from colorama import Fore, Style, init
from modules.metadata import extract_metadata
from modules.network import network_recon
from modules.hasher import generate_hashes

# Initialize colorama
init(autoreset=True)

BANNER = f"""{Fore.BLUE}
██╗   ██╗ █████╗ ██╗     ██╗  ██╗██╗   ██╗██████╗ ██╗███████╗
██║   ██║██╔══██╗██║     ██║ ██╔╝╚██╗ ██╔╝██╔══██╗██║██╔════╝
██║   ██║███████║██║     █████╔╝  ╚████╔╝ ██████╔╝██║█████╗  
╚██╗ ██╔╝██╔══██║██║     ██╔═██╗   ╚██╔╝  ██╔══██╗██║██╔══╝  
 ╚████╔╝ ██║  ██║███████╗██║  ██╗   ██║   ██║  ██║██║███████╗
  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝
{Fore.WHITE}      [ DIGITAL FORENSICS & OSINT FRAMEWORK ]
{Style.RESET_ALL}"""

def main_menu():
    print(BANNER)
    while True:
        print(f"\n{Fore.CYAN}--- MAIN MENU ---{Style.RESET_ALL}")
        print("1. Metadata Extractor (Image)")
        print("2. Network Recon (Domain)")
        print("3. Hash Generator (File Integrity)")
        print("4. Exit")
        
        choice = input(f"\n{Fore.BLUE}[INPUT]{Style.RESET_ALL} Select an option: ")
        
        if choice == '1':
            path = input(f"{Fore.BLUE}[INPUT]{Style.RESET_ALL} Enter image path: ")
            extract_metadata(path)
        elif choice == '2':
            domain = input(f"{Fore.BLUE}[INPUT]{Style.RESET_ALL} Enter domain: ")
            network_recon(domain)
        elif choice == '3':
            path = input(f"{Fore.BLUE}[INPUT]{Style.RESET_ALL} Enter file path: ")
            generate_hashes(path)
        elif choice == '4':
            print(f"{Fore.YELLOW}[REPORT]{Style.RESET_ALL} Shutting down VALKYRIE...")
            sys.exit()
        else:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid option.")

if __name__ == "__main__":
    main_menu()
