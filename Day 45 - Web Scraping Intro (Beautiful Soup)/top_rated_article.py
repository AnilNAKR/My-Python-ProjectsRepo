from bs4 import BeautifulSoup
import openpyxl

import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles_s= soup.find_all(name="span", class_="titleline")

articles = []
articles_links = []
articles_scores = []
for article in articles_s:
    article_content = article.find("a")
    # print(article_content.getText())
    articles.append(article_content.getText())
    # print(article_content.get("href"))
    articles_links.append(article_content.get("href"))

articles_score = soup.find_all(name="span", class_="score")
for score in articles_score:
    articles_scores.append(int(score.getText().split()[0]))

print(f"Article Heading: {articles}\n")
print(f"Article Link: {articles_links}\n")
print(f"Articles Score: {articles_scores}\n")

max_upvotes = max(articles_scores)
print(f"Articles with highest score: {max_upvotes}\n")
max_index = articles_scores.index(max_upvotes)
# print(max_index)
print(f"Article: {articles[max_index]}\n")
print(f"Article Link: {articles_links[max_index]}\n")


# Create a new Excel workbook to save the data in excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add the list data to the Excel sheet
for index, value in enumerate(articles_scores):
    sheet.cell(row=index+1, column=1).value = value

# Save the workbook
workbook.save("output.xlsx")
print("Excel file created successfully.")
