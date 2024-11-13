import os
import re

# Đường dẫn đến folder chứa các file txt gốc
input_folder = r"C:\Users\LENOVO\Craw_data\Hust-Data-Crawler\Clean_data"
# Đường dẫn đến folder lưu các file txt sau khi loại bỏ link
output_folder = r"C:\Users\LENOVO\Craw_data\Hust-Data-Crawler\New_clean_data"

# Tạo folder output nếu chưa tồn tại
os.makedirs(output_folder, exist_ok=True)

# Biểu thức regex để nhận diện các link
url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

# Lặp qua từng file trong folder gốc
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_path = os.path.join(input_folder, filename)
        
        # Đọc nội dung file
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Loại bỏ link bằng regex
        cleaned_content = re.sub(url_pattern, "", content)
        
        # Lưu nội dung đã xử lý vào file mới trong folder output
        output_path = os.path.join(output_folder, filename)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(cleaned_content)

print("Đã xử lý xong tất cả các file!")
