import os
from typing import Dict, Optional
import requests

COOKIES = {"session": os.environ.get("SESSION_COOKIE")}

def download_url_to_file(url: str, filename: str, cookies: Optional[Dict[str, str]] = None):
    r = requests.get(url, cookies=cookies)
    with open(filename, "w") as f:
        f.write(r.text)
    print(f"Saved to {filename}")

def cd_pyfile():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

def get_file_content(filename: str) -> str:
    with open(filename, "r") as f:
        content = f.read()
    return content
