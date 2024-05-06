import requests
from bs4 import BeautifulSoup
import openpyxl
import os

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url=os.environ.get('bpedia'), headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

girl_details = soup.select("main ul li a")
names = []
for name in girl_details:
    # print(name.getText())
    names.append([name.getText(), name.get("href")])

# # print(names)
# print(len(names))
wb = openpyxl.Workbook()
ws = wb.active

for row_data in names:
    ws.append(row_data)

wb.save("output.xlsx")
