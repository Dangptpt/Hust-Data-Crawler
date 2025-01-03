from utils.pdf import download_file, extract_text_from_url
import csv

# quychedaotao_url = 'https://ctt.hust.edu.vn/Upload/Nguyen%20Quoc%20Dat/files/DTDH_QDQC/Hoctap/QCDT-2023-upload.pdf'
# quydinhngoaingu_url = 'https://ctt.hust.edu.vn/Upload/Nguyen%20Quoc%20Dat/files/DTDH_QDQC/Hoctap/QD_ngoai_ngu_tu_K68_CQ_final.pdf'

# quychedaotao_text = extract_text_from_url(quychedaotao_url)
# quydinhngoaingu_text = extract_text_from_url(quydinhngoaingu_url)

# data_csv = [
#     {
#         'title': 'Quy chế đào tạo',
#         'content': quychedaotao_text,
#     },
#     {
#         'title': 'Quy định ngoại ngữ',
#         'content': quydinhngoaingu_text,
#     }
# ]

# with open('raw_data/quyche.csv', 'w', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=['title', 'content'])
#     writer.writeheader()
#     writer.writerows(data_csv)

ks_url= 'https://ctt.hust.edu.vn/Upload/Nguyen%20Quoc%20Dat/files/DTDH_QDQC/Hoctap/01_3%20HD%20hoc%20chuyen%20tiep%20ky%20su%20180%20TC_Final.pdf'

ks_text = extract_text_from_url(ks_url)

data_csv = [
    {
        'title': 'KSCS',
        'content': ks_text,
    },
   
]

with open('raw_data/KSCS.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'content'])
    writer.writeheader()
    writer.writerows(data_csv)