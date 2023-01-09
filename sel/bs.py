from bs4 import BeautifulSoup as bs
import os, csv

csv_file = open('data.csv', 'w', newline='', encoding='UTF-8')
cols = ['name', 'brand', 'category', 'sales_volume', 'sales_volume_per_unit', 'new', 'termination', 'cost']
csv_writer = csv.DictWriter(csv_file, fieldnames=cols)
csv_writer.writeheader()

success_count = 0
fail_count = 0
report_dir = 'report/'
for file in os.listdir(report_dir):
    try:
        data = {}

        file_path = os.path.join(report_dir, file)
        f = open(file_path, 'r', encoding='UTF-8')
        soup = bs(f, 'html.parser')
        data['name'] = soup.select_one('#frm > div:nth-child(12) > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(1)').find_all(text=True, recursive=False)[1].strip()
        data['brand'] = soup.select_one('#frm > div:nth-child(12) > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2)').find_all(text=True, recursive=False)[1].strip()
        data['category'] = soup.select_one('#frm > div:nth-child(12) > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(4)').find_all(text=True, recursive=False)[0].strip()
        data['sales_volume'] = soup.select_one('#frm > div:nth-child(13) > div > table:nth-child(8) > tbody > tr:nth-child(1) > td:nth-child(3)').get_text()
        data['sales_volume_per_unit'] = soup.select_one('#frm > div:nth-child(13) > div > table:nth-child(8) > tbody > tr:nth-child(1) > td:nth-child(4)').get_text()
        data['new'] = soup.select_one('#frm > div:nth-child(13) > div > table:nth-child(6) > tbody:nth-child(5) > tr:nth-child(1) > td:nth-child(2)').get_text()
        term1 = int(soup.select_one('#frm > div:nth-child(13) > div > table:nth-child(6) > tbody:nth-child(5) > tr:nth-child(1) > td:nth-child(3)').get_text())
        term2 = int(soup.select_one('#frm > div:nth-child(13) > div > table:nth-child(6) > tbody:nth-child(5) > tr:nth-child(1) > td:nth-child(4)').get_text())
        term3 = int(soup.select_one('#frm > div:nth-child(13) > div > table:nth-child(6) > tbody:nth-child(5) > tr:nth-child(1) > td:nth-child(5)').get_text())
        data['termination'] = term1 + term2 + term3
        data['cost'] = soup.select_one('#frm > div:nth-child(15) > div > table:nth-child(2) > tbody > tr > td:nth-child(5)').get_text()
        
        csv_writer.writerow(data)
        f.close()
        success_count += 1
    except:
        fail_count += 1
        print(file)

csv_file.close()
print(f'성공: {success_count}, 실패: {fail_count}')