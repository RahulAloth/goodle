import streamlit as st
import os
from goodle_core import (
    index_files,
    search,
    export_index,
    import_index,
    GOODLE_DATA_DIR
)

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="Goodle Search Engine",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Goodle — Local Search Engine")
st.caption("Google for your hard disk. But lightweight, local, and actually yours.")

# -----------------------------
# Ensure data directory exists
# -----------------------------
if not os.path.exists(GOODLE_DATA_DIR):
    os.makedirs(GOODLE_DATA_DIR, exist_ok=True)

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.header("⚙️ Settings")

recency_weight = st.sidebar.slider(
    "Recency Weight",
    0.0, 1.0, 0.2, 0.05
)

max_results = st.sidebar.slider(
    "Max Search Results",
    1, 20, 5
)

# -----------------------------
# File Upload Section
# -----------------------------
st.sidebar.subheader("📤 Upload Files")

uploaded_files = st.sidebar.file_uploader(
    "Add documents to Goodle",
    type=["pdf", "png", "jpg", "jpeg", "txt", "md"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        save_path = os.path.join(GOODLE_DATA_DIR, file.name)
        with open(save_path, "wb") as f:
            f.write(file.read())
    st.sidebar.success(f"Uploaded {len(uploaded_files)} file(s).")

# -----------------------------
# Re-index Button
# -----------------------------
if st.sidebar.button("🔄 Re-index Files"):
    count = index_files()
    st.sidebar.success(f"Indexed {count} files.")

# -----------------------------
# Import / Export Index
# -----------------------------
st.sidebar.subheader("💾 Index Persistence")

if st.sidebar.button("Export Index"):
    export_index()
    st.sidebar.success("Index exported to goodle_index.json")

if st.sidebar.button("Import Index"):
    import_index()
    st.sidebar.success("Index loaded from goodle_index.json")

# -----------------------------
# Search Bar
# -----------------------------
query = st.text_input("🔎 Search your files", placeholder="Type keywords...")

if query:
    results = search(query, top_n=max_results, recency_weight=recency_weight)

    if not results:
        st.warning("No results found.")
    else:
        st.subheader(f"Results for: **{query}**")

        for r in results:
            file_path = r["path"]
            file_name = os.path.basename(file_path)
            ext = file_name.lower().split(".")[-1]

            st.markdown(f"### 📄 {file_name}")
            st.markdown(f"**Score:** {r['score']:.2f}")
            st.markdown(r["snippet"])

            if ext in ["png", "jpg", "jpeg"]:
                st.image(file_path)

            elif ext == "pdf":
                with open(file_path, "rb") as f:
                    st.download_button("📄 Open PDF", f, file_name)

            elif ext in ["txt", "md"]:
                with open(file_path, "r", encoding="utf-8") as f:
                    st.code(f.read(), language="text")

            st.markdown("---")
