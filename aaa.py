from bs4 import BeautifulSoup
import requests
import pandas as pd

# Gửi yêu cầu GET
response = requests.get('https://soict.hust.edu.vn/thuc-tap-doanh-nghiep.html')

# Kiểm tra mã trạng thái của phản hồi
if response.status_code == 200:
    # Nếu trạng thái là 200, lấy nội dung HTML
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Hàm đệ quy duyệt qua HTML DOM
    def dfs(element):
        for child in element.children:
            if child.name == 'table':
                # Chuyển bảng HTML thành Markdown
                table_html = str(child)
                df = pd.read_html(table_html)[0]
                print(df.to_markdown(index=False))  # Bảng dưới dạng markdown
                continue

            elif child.name == 'a':  # Nếu là thẻ liên kết
                href = child.get('href', '')
                text = child.get_text(strip=True)
                print(f"{text} (Link: {href})")  # In ra văn bản + link

            elif child.name:  # Nếu là các thẻ khác (văn bản có thẻ)
                dfs(child)
            
            else:  # Nếu là văn bản thuần túy
                text = child.text.strip()
                if text:
                    print(text)  # In ra văn bản thuần túy

    # Duyệt qua toàn bộ nội dung HTML
    dfs(soup)

else:
    print(f"Error: {response.status_code} - {response.text}")  # In ra mã trạng thái và nội dung phản hồi
