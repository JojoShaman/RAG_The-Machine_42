from .loader import load_repo
from .chunking import chunk_file
from collections import Counter
from pathlib import Path

if __name__ == "__main__":
    docs = load_repo('data/raw')
    chunks = chunk_file(docs[0])
    for chunk in chunks:
        print(chunk["text"], "\n--")
