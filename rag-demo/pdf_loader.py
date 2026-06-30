from pathlib import Path
import fitz

# Projekt könyvtára
BASE_DIR = Path(__file__).resolve().parent

# PDF-ek mappája
DOCUMENTS_DIR = BASE_DIR / "documents_bands"

if not DOCUMENTS_DIR.exists():
    raise FileNotFoundError(f"Directory not found: {DOCUMENTS_DIR}")

documents = []

# Minden PDF beolvasása
for pdf_file in sorted(DOCUMENTS_DIR.glob("*.pdf")):

    print(f"Loading: {pdf_file.name}")

    pdf = fitz.open(pdf_file)

    for page_number, page in enumerate(pdf, start=1):

        text = page.get_text().strip()

        if not text:
            continue

        documents.append(
            {
                "source_file": pdf_file.name,
                "page": page_number,
                "text": text,
            }
        )

    pdf.close()

print(f"\nLoaded {len(documents)} pages.\n")

# Ellenőrzésként kiírjuk az első oldalt
first = documents[0]

print("Source:", first["source_file"])
print("Page:", first["page"])
print(first["text"][:1000])