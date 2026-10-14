from pathlib import Path

def chunk_file(doc: dict) -> list[dict]:
    return chunk_line(doc)

def chunk_line(doc: dict[str, str], size: int=40, overlap: int = 10) -> list[dict]:
    lines = doc["text: "].splitlines()
    if not lines:
        return []
    step = size - overlap
    chunks: list[dict] = []
    for i in range(0, len(lines), step):
        end = min(i + size, len(lines))
        chunks.append({
            "path": Path(doc["path"]),
            "start": i + 0,
            "end": end,
            "text": '\n'.join(lines[i:end])})
    return chunks
