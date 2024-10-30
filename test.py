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
# url = "https://soict.hust.edu.vn/huong-dan-thuc-hien-thuc-tap-doanh-nghiep-cho-hoc-vien-cao-hoc-ky-2024-1.html"
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, "html.parser")

    # Trích xuất tiêu đề và văn bản
#    title = soup.find('h1', class_='entry-title').get_text(strip=True)
#    title = soup.find('h1').get_text(strip=True)
    # title = soup.find('span', class_ = "breadcrumb_last").get_text(strip=True)
    # main_text = soup.find("div", class_='entry-content single-page')
    # print(main_text)
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

from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        
        {"role": "user", "content": ''' 
Title: Hướng dẫn làm Thẻ gửi xe và làm vé xe buýt tháng
I. Làm thẻ gửi xe đạp, xe máy trong khuôn viên trường
1. Đăng ký làm thẻ gửi xe thường xuyên
Từ K64 trở đi Nhà trường đã tích hợp thẻ gửi xe trong thẻ sinh viên, do vậy sinh viên có thể đăng ký làm thẻ gửi xe bằng cách: Sinh viên trực tiếp đến Trung tâm Dịch vụ và hỗ trợ Bách khoa để nạp tiền đăng ký thẻ gửi xe.
Sau khi sinh viên đăng ký làm thẻ gửi xe, Trung tâm Dịch vụ và hỗ trợ Bách khoa sẽ kích hoạt mã gửi xe trên hệ thống và sinh viên bắt đầu sử dụng thẻ sinh viên để gửi xe tại các nhà xe trong khuôn viên trường.
2. Gửi xe không thường xuyên: Các trường hợp không sử dụng vé thường xuyên sẽ trực tiếp trả tiền gửi xe tại Nhà gửi xe
3. Mức phí gửi xe: 
Mức phí gửi xe đạp, xe máy hiện thực hiện theo Quyết định số 44/2017/QĐ-UBND ngày 15/12/2017 của UBND Thành phố Hà Nội áp dụng đối với khu vực trường học. Cụ thể như sau: 
| 0              | 1                           | 2                       |
|:---------------|:----------------------------|:------------------------|
| Loại xe        | Thường xuyên (đồng/xe/lượt) | Vãng lai (đồng/xe/lượt) |
| Xe đạp         | 1.000                       | 2.000                   |
| Xe máy         | 2.000                       | 3.000                   |
| Xe đạp sau 18h | 2.000                       | 3.000                   |
| Xe máy sau 18h | 4.000                       | 4.000                   |
         
Dựa vào context trên, hãy trả lời câu hỏi sau:

Anh gửi xe máy lúc 10h tối hết bao tiền em ơi?'''},
    ],
)
print(completion.choices[0].message.content)
