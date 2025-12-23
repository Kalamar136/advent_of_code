import os
from typing import Dict, Optional
import requests
from pathlib import Path

COOKIES = {"session": os.environ.get("SESSION_COOKIE")}
DOCUMENT_URL= "https://adventofcode.com/2015/day/{day}/input"

def get_input_path(input_name: str, aoc_year_path: Path) -> Path:
    return aoc_year_path / "input_files" / f"{input_name}.txt"

def download_url_to_file(url: str, file_path: Path, cookies: Optional[Dict[str, str]] = None) -> None:
    r = requests.get(url, cookies=cookies)

    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        f.write(r.text)
    print(f"Saved to {file_path}")

def get_file_content(filename: Path) -> str:
    with open(filename, "r") as f:
        content = f.read()
    return content
