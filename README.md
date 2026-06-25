# 🌟 Goodle — A Lightweight Local Search Engine (With Docker Support)

Goodle is a simple, fast, privacy‑friendly local search engine that runs entirely on your computer — specifically on the folder you choose.
It indexes your documents (PDFs, text files, images, Word files, CSVs) and lets you search them instantly through a clean Streamlit UI.

Goodle exists for one reason:
we all dump files into one folder and forget what’s inside.

Students, office workers, note‑takers — anyone who collects screenshots, quick text notes, meeting summaries, reference PDFs — eventually faces the same problem:
“Where did I save that thing?”

I’ve been there too. During long meetings I jot things down in text files, save screenshots, download PDFs, and throw everything into one folder. Days later, when I need something, I don’t remember the file name, the format, or even whether it was a screenshot or a document.

That’s where Goodle shines.

Use whatever is fastest for you — TextPad, Word, a screenshot, a random PDF — just drop it in your folder.
Goodle will index it.  
Then you simply search with any keyword you remember.
Even if the content is inside an image, Goodle finds it.

Is it cool? 🌟 🌟

Are there AI tools that do similar things?
Sure — but Goodle is simple, local, lightweight, and powerful without the complexity.

Developers are welcome to edit, extend, and enhance Goodle.
If you find bugs, tell me — I’ll fix them.
Until then, enjoy your cup of tea.
---

## 📁 Folder Structure

goodle/  
├── goodle_core.py — Search + indexing logic  
├── streamlit_app.py — UI (Streamlit)  
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

git clone https://github.com/yourname/goodle  
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

## 📂 How to Change the Folder Goodle Indexes

Goodle indexes whatever folder you mount into the container.

### Step 1 — Edit docker-compose.yml

Find this section:

volumes:  
  - /home/rahul/crf_user_guide:/app/goodle_data  

Replace `/home/rahul/crf_user_guide` with your new folder path.

Example:

volumes:  
  - /home/rishaan/my_documents:/app/goodle_data  

### Step 2 — Restart Goodle

docker compose down  
docker compose up -d  

Goodle will re‑index the new folder automatically.

---

## 🎁 Release Version (For Non‑Technical Users)

If you want to give Goodle to someone who doesn’t want to compile or build, they only need:

- Docker Desktop installed  
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
- I am busy, you are welcome to do any modifications. 

---

## 🎉 Goodle is Ready for Use
