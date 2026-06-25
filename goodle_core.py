import os
import json
import re
import pdfplumber
from PIL import Image
import pytesseract
import nltk
from nltk.corpus import stopwords
from collections import defaultdict

# -----------------------------
# Fixed data directory inside Docker
# -----------------------------
GOODLE_DATA_DIR = "/app/goodle_data"

# -----------------------------
# Safe NLTK Loader
# -----------------------------
def safe_download(resource, package=None):
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(package or resource.split("/")[-1])

safe_download("tokenizers/punkt", "punkt")
safe_download("tokenizers/punkt_tab", "punkt_tab")
safe_download("corpora/stopwords", "stopwords")

stop_words = set(stopwords.words("english"))

# -----------------------------
# In-Memory Index
# -----------------------------
goodle_index = {}

# -----------------------------
# Extraction Functions
# -----------------------------
def extract_text_from_pdf(filepath):
    text = ""
    try:
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"[PDF ERROR] {filepath}: {e}")
    return text

def extract_text_from_image(filepath):
    try:
        img = Image.open(filepath)
        return pytesseract.image_to_string(img)
    except Exception as e:
        print(f"[IMAGE ERROR] {filepath}: {e}")
        return ""

def extract_text_from_text_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[TEXT ERROR] {filepath}: {e}")
        return ""

def get_file_content(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    if ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(filepath)
    if ext in [".txt", ".md"]:
        return extract_text_from_text_file(filepath)
    return None

# -----------------------------
# Indexing
# -----------------------------
def index_files():
    global goodle_index
    goodle_index = {}

    if not os.path.exists(GOODLE_DATA_DIR):
        os.makedirs(GOODLE_DATA_DIR, exist_ok=True)

    files = []
    for root, _, filenames in os.walk(GOODLE_DATA_DIR):
        for name in filenames:
            path = os.path.join(root, name)
            ext = os.path.splitext(name)[1].lower()

            if ext not in [".pdf", ".png", ".jpg", ".jpeg", ".txt", ".md"]:
                continue

            files.append(path)

    for f in files:
        text = get_file_content(f)
        if text:
            goodle_index[f] = text

    return len(goodle_index)

# -----------------------------
# Tokenization + Frequency
# -----------------------------
def tokenize_text(text):
    tokens = nltk.word_tokenize(text.lower())
    return [t for t in tokens if t.isalpha() and t not in stop_words]

def calculate_keyword_frequency(text):
    freq = defaultdict(int)
    for t in tokenize_text(text):
        freq[t] += 1
    return freq

# -----------------------------
# Snippet Highlighting
# -----------------------------
def highlight_text(text, query_tokens, snippet_length=200):
    text_lower = text.lower()
    best_snippet = text[:snippet_length]

    max_hits = -1
    for i in range(0, len(text) - snippet_length, 50):
        window = text[i:i+snippet_length]
        hits = sum(window.lower().count(q) for q in query_tokens)
        if hits > max_hits:
            max_hits = hits
            best_snippet = window

    snippet = best_snippet
    for q in query_tokens:
        snippet = re.sub(rf"\\b{q}\\b", f"**{q}**", snippet, flags=re.IGNORECASE)

    return snippet

# -----------------------------
# Search Engine
# -----------------------------
def search(query, top_n=5, recency_weight=0.2):
    if not goodle_index:
        return []

    query_tokens = tokenize_text(query)
    if not query_tokens:
        return []

    results = []
    mtimes = []

    for path, content in goodle_index.items():
        freq = calculate_keyword_frequency(content)
        score = sum(freq[q] for q in query_tokens)

        if score > 0:
            mtime = os.path.getmtime(path)
            mtimes.append(mtime)
            results.append({
                "path": path,
                "content": content,
                "score": score,
                "mtime": mtime
            })

    if not results:
        return []

    min_m, max_m = min(mtimes), max(mtimes)

    for r in results:
        if max_m > min_m:
            recency = (r["mtime"] - min_m) / (max_m - min_m)
            r["score"] += recency_weight * recency

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    for r in results[:top_n]:
        r["snippet"] = highlight_text(r["content"], query_tokens)

    return results[:top_n]

# -----------------------------
# Persistence
# -----------------------------
def export_index(filename="goodle_index.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(goodle_index, f, indent=4)

def import_index(filename="goodle_index.json"):
    global goodle_index
    with open(filename, "r", encoding="utf-8") as f:
        goodle_index = json.load(f)
