
from pathlib import Path
import pdfplumber


SUPPORTED = {".txt", ".pdf", ".docx"}


def load_policy(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    extension = path.suffix.lower()

    if extension == ".txt":
        text = read_txt(path)
    elif extension == ".pdf":
        text = read_pdf(path)
    elif extension == ".docx":
        text = read_docx(path)
    else:
        raise ValueError(f"Unsupported file type: {extension}")

    return clean_text(text)

def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    cleaned = [line for line in lines if line]
    return "\n".join(cleaned)

def read_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

def read_pdf(path: Path) -> str:
    text_parts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    return "\n".join(text_parts)

def read_docx(path: Path) -> str:
    from docx import Document
    doc = Document(path)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    return "\n".join(paragraphs)
