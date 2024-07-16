from bs4 import BeautifulSoup
import lxml

my_file = open(file='website.html')
html_content = my_file.read()
my_file.close()

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.title)
print(soup.h1)
print(soup.li) # this is the first <li> tag

all_anchor_tags = soup.find_all(name='a')  # a list of all anchor tags
print(all_anchor_tags)

print()
for tag in all_anchor_tags:
    print(f'{tag.getText()} -- {tag.get("href")}')
print()

heading_name = soup.find(name='h1', id='name')  # an <h1 id='name'></h1> element
print(heading_name)
print()

name = soup.select_one(selector='#name')  # select an element by id
print(name)

anchors_in_a_list = soup.select('li a')
print(anchors_in_a_list)

