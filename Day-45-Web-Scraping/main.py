from bs4 import BeautifulSoup
# import lxml

# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # soup = BeautifulSoup(contents, 'html.parser')

# # Return title element
# print(soup.title)
# # Returns tag name
# print(soup.title.name)
# #  Returns title content
# print(soup.title.string)

# Used for printing entire web page code in the output line by line w/o indentation
# print(soup)

# # Used for indenting html output in a proper way
# print(soup.prettify())

#  To get all of the anchor tags and all para's in the website
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#
#     # for getting all the href links
#     print(tag.get("href"))

# # To hold element by id's
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# # To hold elements using class attribute
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# # To hold elements using css selector
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# # To select elements that have an id
# name = soup.select_one(selector="#name")
# print(name)
#
# # To select headings that have class
# heading = soup.select(".heading")
# print(heading)