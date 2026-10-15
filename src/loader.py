from pathlib import Path

SKIP_DIRS = {".git", "node_modules", "__pychache__", ".venv", "build", "dist"}
EXTS = {".py", ".md", ".txt"}

def load_repo(root: str) -> list[dict]:
    docs: list[dict] = []
    for path in Path(root).rglob('*'):
        if not path.is_file() or path.suffix not in EXTS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeEncodeError:
            continue
        docs.append({"path": str(path.relative_to(root)), "text: ": text})
    return docs