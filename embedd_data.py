from supabase import create_client, Client
import torch
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import os 

# Khởi tạo kết nối Supabase
url= "https://kpqiroscjnqqywwbsmlm.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtwcWlyb3Njam5xcXl3d2JzbWxtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzA2MDQzNjMsImV4cCI6MjA0NjE4MDM2M30.alP9f7fhBQ2CFOpGkiFb0z4rsSyCNERe6Xo_kncQKrI"

try:
    supabase: Client = create_client(url, key)
except Exception as e:
    print("Error connecting to Supabase:", e)

# Load model BGE-M3
model = SentenceTransformer("BAAI/bge-m3")

data = supabase.table("document_v1").select("id", "embed_doc").execute().data

embeddings = []
for entry in data:
    text = entry['embed_doc']
    vector = model.encode(text)
    # print(embeddings )
    # Thêm id và vector vào danh sách embeddings
    embeddings.append({"id": entry["id"], "vector": vector.tolist()})

# Bước 3: Insert vector embedding vào bảng 2
for embedding in embeddings:
    supabase.table("embedding_v1").insert({"id": embedding["id"], "vector": embedding["vector"]}).execute()
print("complete!!")