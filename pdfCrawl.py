import pdfplumber
import requests
# Đường dẫn tới file PDF và file text
pdf_file_path = "student_handbook.pdf"
text_file_path = "Clean_data/QuyDinhSOICT.txt"
url = "https://soict.hust.edu.vn/wp-content/uploads/So-tay-Sinh-vien-Truong-CNTT-V2.0.pdf"
response = requests.get(url)

# Lưu file PDF tạm thời
with open(pdf_file_path, "wb") as file:
    file.write(response.content)

# Mở file PDF
with pdfplumber.open(pdf_file_path) as pdf:
    # Tạo một chuỗi chứa nội dung
    all_text = ""
    
    # Lặp qua tất cả các trang của PDF
    for page in pdf.pages:
        all_text += page.extract_text()  # Trích xuất nội dung văn bản

# Ghi văn bản vào file text
with open(text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(all_text)

print("Văn bản đã được ghi vào file text.")
