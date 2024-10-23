from docx import Document
import pandas as pd

# Đường dẫn tới file .docx
file_path = r'Quy trình TTDN_SV.docx'

# Mở file .docx
doc = Document(file_path)

# Mở file markdown để ghi
with open('Textfile/Quy trình TTDN_SV.txt', 'w', encoding='utf-8') as f:
    for element in doc.element.body:
        if element.tag.endswith('p'):  # Nếu phần tử là đoạn văn
            paragraph = element.text.strip()
            if paragraph:  # Ghi chỉ nếu đoạn văn không rỗng
                f.write(paragraph + '\n\n')  # Giữ khoảng cách giữa các đoạn văn

        elif element.tag.endswith('tbl'):  # Nếu phần tử là bảng
            # Ghi tiêu đề bảng
            f.write("### Table:\n\n")

            # Lấy bảng tương ứng từ doc.tables
            table = doc.tables[0]  # Giả sử bạn muốn lấy bảng đầu tiên

            # Chuyển đổi bảng thành DataFrame
            data = []
            for row in table.rows:
                row_data = [cell.text.strip() for cell in row.cells]
                data.append(row_data)
            
            # Chuyển đổi danh sách thành DataFrame
            df = pd.DataFrame(data)

            # Ghi DataFrame ở định dạng Markdown
            f.write(df.to_markdown(index=False))  # Sử dụng showindex=False
            f.write("\n\n" + "-" * 50 + "\n")  # Phân cách giữa các bảng

print("Đã ghi nội dung vào 'output.md'.")
