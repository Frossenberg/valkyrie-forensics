from PIL import Image
from PIL.ExifTags import TAGS
from colorama import Fore, Style

def extract_metadata(image_path):
    print(f"{Fore.BLUE}[ANALYSIS]{Style.RESET_ALL} Extracting metadata from: {image_path}")
    try:
        image = Image.open(image_path)
        info = image._getexif()
        if info:
            print(f"{Fore.GREEN}[EVIDENCE]{Style.RESET_ALL} Metadata found:")
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                print(f"  {Fore.CYAN}{decoded}:{Style.RESET_ALL} {value}")
        else:
            print(f"{Fore.YELLOW}[REPORT]{Style.RESET_ALL} No EXIF data found in this image.")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Failed to extract metadata: {e}")
