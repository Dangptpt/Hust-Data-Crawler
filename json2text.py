import requests
from bs4 import BeautifulSoup
import pandas as pd
import re 


    
def dfs(element, depth=0, output_file=None):
    buffer = ""
    for child in element.children:
        if child.name == 'table':
            table_html = str(child)
            df = pd.read_html(table_html)[0]
            output_file.write(df.to_markdown(index=False) + '\n\n')  # Ghi bảng vào file
            continue

        if child.name: 
            buffer += dfs(child, depth + 1, output_file)  # Đệ quy để duyệt tiếp các thẻ con
        else:
            text = child.text.strip()
            if re.match(r'^\d+\.', text):  # Tìm các đề mục dạng 1., 2., ...
                if buffer:  # Nếu có văn bản trước đó, ghi vào file trước khi tiếp tục
                    output_file.write(buffer.strip() + '\n\n')
                buffer = text  # Lưu đề mục mới vào buffer
            else:
                buffer += " " + text  # Tích lũy văn bản tiếp theo sau đề mục

    return buffer

# URL và yêu cầu truy xuất
url = "https://soict.hust.edu.vn/thong-tin-tuyen-sinh-2024.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('span', class_ = "breadcrumb_last").get_text(strip=True)
    main_text = soup.find("div", class_='entry-content single-page')

    with open(f'Textfile/{title}.txt', 'w', encoding='utf-8') as f:
        result = dfs(main_text, output_file=f)
        if result.strip():  # Ghi đoạn văn cuối cùng nếu có
            f.write(result.strip() + '\n\n')




