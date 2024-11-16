#!/usr/bin/python3

import fitz
import sys
from pathlib import Path

def main():
    doc = fitz.open(sys.argv[1])
    pages_text = [page.get_text().replace("\n", "") for page in doc.pages()]
    long_text = "".join(pages_text)
    secrets = [
        open(f).read().strip()
        for f in Path(sys.argv[2]).expanduser().iterdir()
    ]
    for secret in secrets:
        if secret in long_text:
            print("Santa, we have a problem...")
            return
    return 1




if __name__ == "__main__":
    sys.exit(main())
