# 🌟 Goodle — A Lightweight Local Search Engine

<img width="1774" height="887" alt="image" src="https://github.com/user-attachments/assets/48849cce-d061-4b4d-99cd-7e4953006e57" />

Goodle is a simple, fast, privacy‑friendly local search engine that runs entirely on your computer — indexing only the folder you choose. It scans your PDFs, text files, images, Word documents, and CSVs, then lets you search them instantly through a clean Streamlit UI.

We all do it:  
Dump files into one folder… and forget what’s inside.

Students, office workers, note‑takers — anyone who collects screenshots, quick notes, meeting summaries, or reference PDFs eventually faces the same moment:

“Where did I save that thing”

That’s exactly where Goodle shines.

Use whatever is fastest — TextPad, Word, a screenshot, a random PDF — just drop it in your folder.  
Goodle will index it.  
Then you search with any keyword you remember.  
Even if the content is inside an image, Goodle finds it.

Is it cool? 🌟🌟  


---

# 🚀 Quick Start (Recommended)

The easiest way to run Goodle is using the official Docker image from GitHub Container Registry.

### 1️⃣ Install Docker Desktop  

Windows, macOS, or Linux.

### 2️⃣ Pull the Goodle image

```code
docker pull ghcr.io/rahulaloth/goodle:v1.0.0
```

### 3️⃣ Run Goodle

Replace `/path/to/your/folder` with the folder you want Goodle to index:

Windows:

```code
docker run -d -p 8501:8501 -v D:/IdentityCardsDetails:/app/goodle_data ghcr.io/rahulaloth/goodle:v1.0.0
```
Run on Different port

```code
docker run -d -p 8600:8501 -v D:/IdentityCardsDetails:/app/goodle_data ghcr.io/rahulaloth/goodle:v1.0.0
```
Quick check on windows:
To see what is using port 8501:
```code
netstat -ano | findstr :8501
```

Then:
```code
http://localhost:8600
```
Linux:

```code
docker run -d -p 8501:8501 -v /home/Name/IdentityCardsDetails:/app/goodle_data ghcr.io/rahulaloth/goodle:v1.0.0
```
If port 8501 is busy on Linux, use:
```code
docker run -d -p 8600:8501 -v /home/rishaan/IdentityCardsDetails:/app/goodle_data ghcr.io/rahulaloth/goodle:v1.0.0
```
Then Option
```code
http://localhost:8600
```

Open in your browser:

```code
http://localhost:8501
```
That’s it.  
No Python. No setup. No dependencies.

---

# 🐳 Docker Compose (Alternative)

If you prefer using `docker-compose.yml`, create a file like this:

```code
services:
  goodle:
    image: ghcr.io/rahulaloth/goodle:v1.0.0
    ports:
      - "8501:8501"
    volumes:
      - /path/to/your/folder:/app/goodle_data

```

Run:

```code
docker compose up -d

```

---

# 📂 Changing the Indexed Folder

Goodle indexes **whatever folder you mount** into `/app/goodle_data`.

### Linux example

/home/rishaan/my_documents:/app/goodle_data

### Windows example

D:/goodleTest:/app/goodle_data

✔ Use forward slashes  
✔ No backslashes  
✔ No double slashes  

Restart Goodle:

docker compose down  
docker compose up -d

Or press **Re‑Index** in the UI.

---

# 📦 Supported File Types

Goodle can index:

- PDF files  
- Text files (.txt, .md)  
- Word documents (.docx)  
- Images (.png, .jpg, .jpeg)  
- CSV files  

Not recommended:  
- Excel (.xlsx) — structured data, not text  

---

# 🧱 Developer Setup

If you want to modify Goodle:

```code
git clone https://github.com/RahulAloth/goodle
cd goodle  
pip install -r requirements.txt  
streamlit run goodle_app.py

```

Rebuild Docker image after changes:


```code
docker compose build  
docker compose up -d
```

Full rebuild:

```code
docker compose down --rmi all  
docker compose build  
docker compose up -d
```

---

# 🧭 Troubleshooting

### Check if Goodle is running

```code
docker ps

```

### View logs

```code
docker compose logs -f

```
### Stop Goodle

```code
docker compose down

```

---

# 📁 Folder Structure

goodle/  
├── goodle_core.py        # Search + indexing logic  
├── goodle_app.py         # Streamlit UI  
├── requirements.txt      # Python dependencies  
├── Dockerfile            # Build Goodle container  
├── docker-compose.yml    # Example compose file  
└── README.md             # Documentation  

---

# 🧩 Future Enhancements

- Faster indexing  
- More file types  
- Improved UI  
- Smarter ranking  
- Plugin system  

Goodle is intentionally simple so you can build on top of it.

---

# 🎉 Goodle is Ready for Use

If you find bugs or want to contribute, feel free to open an issue or PR.  
Enjoy your cup of tea ☕ while Goodle finds your lost files.
