import os
import re
from pdfminer.high_level import extract_text
import requests
import uuid
from urllib.parse import urlparse


def get_filename_from_url(url):
    # Phân tích URL
    parsed_url = urlparse(url)
    # Lấy phần đường dẫn từ URL
    path = parsed_url.path
    # Lấy tên file từ đường dẫn
    filename = os.path.basename(path)
    return filename


def download_file(url, local_filename):
    response = requests.get(url)
    print(response.status_code)
    with open(local_filename, "wb") as f:
        f.write(response.content)
    return response.headers.get('Content-Type')

def get_content_type(url):
    try:
        # Gửi yêu cầu HEAD để lấy thông tin tiêu đề mà không tải xuống toàn bộ nội dung
        response = requests.head(url, allow_redirects=True)
        print(response.status_code)
        # Lấy giá trị Content-Type từ tiêu đề
        content_type = response.headers.get('Content-Type', '').lower()
        return content_type
    except requests.RequestException as e:
        print(f"Lỗi khi kiểm tra URL: {e}")
        raise e


def extract_text_from_url(url):
    uuid4 = uuid.uuid4()
    temp_filename = "temp" + str(uuid4)
    content_type = download_file(url, temp_filename)

    if "application/pdf" in content_type:
        temp_filename += ".pdf"
        os.rename("temp" + str(uuid4), temp_filename)
        text = extract_text(temp_filename)
    elif "text/plain" in content_type:
        temp_filename += ".txt"
        os.rename("temp" + str(uuid4), temp_filename)
        with open(temp_filename, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        os.remove("temp" + str(uuid4))
        raise ValueError("Unsupported file type")

    # Xóa file tạm thời sau khi xử lý
    os.remove(temp_filename)

    return text

import camelot

def read_table(pdf_path):
    uuid4 = uuid.uuid4()
    temp_filename = "temp" + str(uuid4)
    content_type = download_file(pdf_path, temp_filename)

    if "application/pdf" in content_type:
        temp_filename += ".pdf"
        os.rename("temp" + str(uuid4), temp_filename)
        # Trích xuất bảng từ file PDF
        tables = camelot.read_pdf(temp_filename, pages='all')

        # Chuyển bảng đầu tiên sang Markdown
        markdown_table = tables[0].df.to_markdown(index=False)

    # Xóa file tạm thời sau khi xử lý
    os.remove(temp_filename)
    
    return markdown_table   
