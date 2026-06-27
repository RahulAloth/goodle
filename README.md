# 🌟 Goodle — A Lightweight Local Search Engine

<img width="1774" height="887" alt="image" src="https://github.com/user-attachments/assets/48849cce-d061-4b4d-99cd-7e4953006e57" />



Goodle is a simple, fast, privacy‑friendly local search engine that runs entirely on your computer — indexing only the folder you choose. It scans your PDFs, text files, images, Word documents, and CSVs, then lets you search them instantly through a clean Streamlit UI.

We all do it:
Dump files into one folder… and forget what’s inside.

Students, office workers, note‑takers — anyone who collects screenshots, quick notes, meeting summaries, or reference PDFs eventually faces the same moment:

    “Where did I save that thing?”

I’ve been there too. During long meetings I jot things down, save screenshots, download PDFs, and throw everything into one folder. Days later, I don’t remember the file name, the format, or even whether it was a screenshot or a document.

That’s exactly where Goodle shines.

Use whatever is fastest — TextPad, Word, a screenshot, a random PDF — just drop it in your folder.
Goodle will index it.
Then you search with any keyword you remember.
Even if the content is inside an image, Goodle finds it.

Is it cool? 🌟🌟
Absolutely.

Are there AI tools that do similar things? Sure — but Goodle is local, lightweight, private, and powerful without the complexity.

Developers are welcome to extend it. If you find bugs, tell me — I’ll fix them. Until then, enjoy your cup of tea.

Usage Example:
---
<img width="1201" height="1012" alt="image" src="https://github.com/user-attachments/assets/1a03d70e-960b-4b44-b9e9-f6c0922c0603" />

## 📁 Folder Structure

goodle/  
├── goodle_core.py — Search + indexing logic  
├── goodle_app.py — UI (Streamlit)  
├── requirements.txt — Python dependencies  
├── Dockerfile — Build Goodle container  
├── docker-compose.yml — Run Goodle with folder mounting  
└── README.md — Documentation  

---

## 📦 Supported File Types

Goodle can index:

- PDF files  
- Text files (.txt, .md)  
- Word documents (.docx)  
- Images (.png, .jpg, .jpeg)  
- CSV files  

Not recommended:  
- Excel (.xlsx) — structured data, not text  

---

## 🧱 Installation (One‑Time Setup)

### 1️⃣ Install Docker Desktop  
Required for Windows, Mac, Linux.

### 2️⃣ Download or Clone Goodle

git clone https://github.com/RahulAloth/goodle  
cd goodle  

### 3️⃣ Build Goodle (only once)

docker compose build  

---

## 🚀 Run Goodle

### ▶️ Start Goodle

docker compose up -d  

Open in browser:

http://localhost:8501

### ⏹ Stop Goodle

docker compose down  

---

## 🔁 After Restarting Your PC

You do NOT need to rebuild Goodle.

Just run:

cd /path/to/goodle  
docker compose up -d  

Goodle will start instantly.

---

## 📂 How to Change the Folder Goodle Indexes - Prerequisites

Goodle indexes **whatever folder you mount into the container**.  
The **left side** of the volume mapping must point to **your local indexing directory** — the folder on your computer that contains the documents you want Goodle to index.

### Edit `docker-compose.yml`

Find this section:

```yaml
volumes:
  - /path/to/your/folder:/app/goodle_data
```

Replace `/path/to/your/folder` with the folder you want Goodle to index.

### Linux example:

```yaml
volumes:
  - /home/rishaan/my_documents:/app/goodle_data
```

### Windows example (correct syntax):

```yaml
volumes:
  - D:/goodleTest:/app/goodle_data
```

✔ Use **forward slashes**  
✔ Do **not** use `\\` or `//`  
✔ Do **not** use backslashes  

### Restart Goodle

```bash
docker compose down
docker compose up -d
```

Goodle will re‑index the new folder (or press the **Re‑Index** button in the UI).

---

## 🎁 Release Version (For Non‑Technical Users)

They only need:
    - Docker Desktop
    - The Goodle folder
    - One file to edit: docker-compose.yml 
### Their steps:

1. Download the Goodle ZIP  
2. Extract it  
3. Open docker-compose.yml  
4. Change this line:

   - /path/to/their/folder:/app/goodle_data  

5. Save the file  
6. Run:

   docker compose up -d  

7. Open:

   http://localhost:8501  

That’s it. No Python. No coding. No setup.

---

## 🧪 Compile Instructions (For Developers)

If you modify code:

docker compose build  
docker compose up -d  

If you only change the folder:

docker compose down  
docker compose up -d  

If you want to rebuild everything:

docker compose down --rmi all  
docker compose build  
docker compose up -d  

---

## 🧭 Troubleshooting

### Check if Goodle is running:

docker ps  

### View logs:

docker compose logs -f  

### Remove containers:

docker compose down  

---

## 🧩 Future Enhancements
- Feel free to add features, improve indexing, or extend the UI.
- Goodle is intentionally simple so you can build on top of it.

---

## 🎉 Goodle is Ready for Use
