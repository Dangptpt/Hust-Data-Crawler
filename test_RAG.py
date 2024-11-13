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


def chat():
    query = input('Nhập câu hỏi: ')

    embedding = model.encode(query).tolist()

    response = supabase.rpc(
        'match_documents_v2',
        {
            'query_embedding': embedding,
            'match_threshold': 0.4,
            'match_count': 5
        }
    ).execute()
    context = ''
    for obj in response.data:
        print(obj)
        context += obj['raw_doc'] + '\n'
    # print(context)

while True:
    chat()