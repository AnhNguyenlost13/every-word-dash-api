#!/usr/bin/env python3

import requests

def fetch_and_extract(url: str, prefix: str = "-> ") -> str:
    resp = requests.get(url)
    resp.raise_for_status()
    
    first_line = resp.text.splitlines()[0]
    
    if prefix in first_line:
        return first_line.split(prefix, 1)[1]
    else:
        return ""
    
def main():
    url = "https://gdcolon.com/ewd_history.txt"
    result = fetch_and_extract(url)
    
    with open("badeline.txt", "w", encoding="utf-8") as f:
        f.write(result)
    
    print(f"todays word: {result}")

if __name__ == "__main__":
    main()
