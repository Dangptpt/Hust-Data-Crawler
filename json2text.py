import requests
from bs4 import BeautifulSoup
import pandas as pd
import re 


    
def dfs(element, depth=0, output_file=None):
    for child in element.children:
        if child.name == 'table':
            table_html = str(child)
            df = pd.read_html(table_html)[0]
            output_file.write(df.to_markdown(index=False) + '\n\n')  # Ghi bảng vào file
            continue

        if child.name: 
            dfs(child, depth + 1, output_file)  # Đệ quy để duyệt tiếp các thẻ con
        else:
            if child.text !='\n' and child.name != 'i':
                text = child.text.strip()
                output_file.write(text + "\n")
        if child.name == 'a':
            output_file.write(child['href'])
    
# def dfs(element, depth=0):
#     #print("  " * depth + f"Thẻ: {element.name}")    
#     for child in element.children:
#         if child.name == 'table':
#             table_html = str(child)
#             df = pd.read_html(table_html)[0]
#             print(df.to_markdown(index=False))
#             continue

#         if child.name: 
#             dfs(child, depth + 1)
#         else:
#             if child.text != '\n':
#                 print(child.text)
#         if child.name == 'a':
#             print(child['href'])



# URL và yêu cầu truy xuất
url = 'https://soict.hust.edu.vn/dang-uy-truong.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find('span', class_ = "breadcrumb_last").get_text(strip=True)
    main_text = soup.find("div", class_='entry-content single-page')
    with open(f'Clean_data/{title}.txt', 'w', encoding='utf-8') as f:
        dfs(main_text, output_file=f)





