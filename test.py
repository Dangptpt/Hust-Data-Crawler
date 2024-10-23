import requests
from bs4 import BeautifulSoup
import json


# Hàm trích xuất dữ liệu bảng
# def extract_tables(soup):
#     tables_data = []
#     tables = soup.find_all('table')
#
#     for table in tables:
#         table_rows = []
#         rows = table.find_all('tr')
#         for row in rows:
#             cells = row.find_all(['td', 'th'])
#             cell_texts = [cell.get_text(strip=True) for cell in cells]
#             table_rows.append(cell_texts)
#         tables_data.append(table_rows)
#     return tables_data


# URL và yêu cầu truy xuất
url = "https://soict.hust.edu.vn/huong-dan-thuc-hien-thuc-tap-doanh-nghiep-cho-hoc-vien-cao-hoc-ky-2024-1.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Trích xuất tiêu đề và văn bản
#    title = soup.find('h1', class_='entry-title').get_text(strip=True)
#    title = soup.find('h1').get_text(strip=True)
    title = soup.find('span', class_ = "breadcrumb_last").get_text(strip=True)
    main_text = soup.find("div", class_='entry-content single-page')
    print(main_text)
#    main_text = soup.find("div", class_='text-justify')

    # Trích xuất bảng
    # tables = extract_tables(soup)

    # Định dạng dữ liệu thành JSON
#     data = {
#         "Topic" : "Thực tập doanh nghiệp cho sinh viên SOICT",
#         "title": title,
#         "main_text": main_text.text,
#         # "tables": [
#         #     {"table_index": idx + 1, "data": table} for idx, table in enumerate(tables)
#         # ]
#     }

#     # Lưu dữ liệu vào file JSON
#     with open("Data/data38.json", "w", encoding="utf-8") as json_file:
#         json.dump(data, json_file, ensure_ascii=False, indent=4)

#     print("Data has been saved to 'web_data.json'")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
