import os
import re
import uuid
import pandas as pd

def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def split_into_chunks(text, max_words=256, type_doc=""):
    words = text.split()
    chunks = []
    current_chunk = [f"{type_doc}: "]

    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= max_words:
            chunks.append(" ".join(current_chunk))
            current_chunk = [f"{type_doc}: "]

    # Thêm phần còn lại nếu còn từ chưa ghép
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def process_files(old_folder, new_folder):
    data = []

    for filename in os.listdir(new_folder):
        old_path = os.path.join(old_folder, filename)
        new_path = os.path.join(new_folder, filename)
        
        if not os.path.isfile(old_path) or not os.path.isfile(new_path):
            continue
        
        # Loại bỏ đuôi .txt khỏi tên file để lấy type_doc
        type_doc = os.path.splitext(filename)[0]
        
        old_text = read_file(old_path)
        new_text = read_file(new_path)
        
        old_paragraphs = [para.strip() for para in old_text.split("\n\n") if para.strip()]
        new_paragraphs = [para.strip() for para in new_text.split("\n\n") if para.strip()]
        
        # for old_para, new_para in zip(old_paragraphs, new_paragraphs):
        #     old_chunks = split_into_chunks(old_para, type_doc=type_doc)
        #     new_chunks = split_into_chunks(new_para, type_doc=type_doc)
            
        #     for raw_chunk, embed_chunk in zip(old_chunks, new_chunks):
        #         data.append({
        #             "id": str(uuid.uuid4()),
        #             "embed_doc": embed_chunk,
        #             "raw_doc": raw_chunk,
        #             "type_doc": type_doc,
        #         })
        for old_para , new_para in zip(old_paragraphs, new_paragraphs):

            data.append({
                "id": str(uuid.uuid4()),
                "embed_doc": f"{type_doc}: " + new_para,
                "raw_doc": f"{type_doc}: " + old_para,
                "type_doc": type_doc,
            })
    return data

# Đường dẫn đến thư mục old_data và new_data
old_folder = r"C:\Users\LENOVO\Craw_data\Hust-Data-Crawler\Clean_data"
new_folder = r"C:\Users\LENOVO\Craw_data\Hust-Data-Crawler\New_clean_data"

# Chạy hàm xử lý
database_ready_data = process_files(old_folder, new_folder)

# Lưu thành file CSV
df = pd.DataFrame(database_ready_data)
df.to_csv("output_chunks.csv", index=False, encoding="utf-8")
