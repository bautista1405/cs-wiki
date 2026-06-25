import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup

links = [
    "https://ppc.cs.aalto.fi/",
    "https://gfxcourses.stanford.edu/cs149/fall23/",
    "https://www.cl.cam.ac.uk/teaching/2122/ConcDisSys/materials.html",
    "https://web.stanford.edu/class/cs143/",
    "http://web.mit.edu/6.033/www/",
    "https://nick-black.com/dankwiki/index.php/Fast_UNIX_Servers",
    "https://nick-black.com/dankwiki/index.php/UNIX_Weapons_School",
    "https://stevens.netmeister.org/631/"
]

output_dir = "/Users/bautistaaramendiapradal/Desktop/programming-wiki/raw/articles/computer-systems-batch-7/"

def slugify(url):
    return url.replace("https://", "").replace("http://", "").replace("/", "_").replace(".", "_").strip("_")

for url in links:
    try:
        print(f"Fetching {url}...")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Get main text content
        text = soup.get_text(separator='\n', strip=True)
        
        filename = f"{slugify(url)}.md"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---\noriginal_url: {url}\nfetched_date: {datetime.now().strftime('%Y-%m-%d')}\n---\n\n")
            f.write(text)
        print(f"Saved to {filepath}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
