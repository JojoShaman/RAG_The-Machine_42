from .loader import load_repo
from .chunking import chunk_file
from collections import Counter
from pathlib import Path
import json


if __name__ == "__main__":
    docs = load_repo('src')
    # for i, d in enumerate(docs):
    #     if Path(d["path"]).suffix == ".py":
    #         print(f"file no: {i} - {d["path"]}")
    chunks = chunk_file(docs[0])
    for chunk in chunks:
        print(chunk["text"], "\n--")