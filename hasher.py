import hashlib
from colorama import Fore, Style

def calculate_hashes(file_path):
    print(f"{Fore.BLUE}[ANALYSIS]{Style.RESET_ALL} Calculating hashes for integrity check: {file_path}")
    try:
        md5_hash = hashlib.md5()
        sha1_hash = hashlib.sha1()
        sha256_hash = hashlib.sha256()

        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha1_hash.update(byte_block)
                sha256_hash.update(byte_block)

        print(f"{Fore.GREEN}[EVIDENCE]{Style.RESET_ALL} File integrity verification complete:")
        print(f"  MD5:    {Fore.CYAN}{md5_hash.hexdigest()}{Style.RESET_ALL}")
        print(f"  SHA1:   {Fore.CYAN}{sha1_hash.hexdigest()}{Style.RESET_ALL}")
        print(f"  SHA256: {Fore.CYAN}{sha256_hash.hexdigest()}{Style.RESET_ALL}")
        
        print(f"{Fore.YELLOW}[REPORT]{Style.RESET_ALL} Hash generation successful.")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} File not found: {file_path}")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Hash calculation failed: {e}")
