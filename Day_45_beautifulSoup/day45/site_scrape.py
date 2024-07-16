from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_site = response.text

soup = BeautifulSoup(yc_site, 'html.parser')
articles = soup.find_all(name="a", class_="storylink")
scores = [int(score.getText()[: score.getText().index(' ')]) for score in soup.find_all(name='span', class_='score')]
# print(scores)

for a in range(len(articles)):
    headline = articles[a].getText()
    link = articles[a].get("href")
    score = scores[a]
    print(f'{headline} ({link}) - {score}')
print('\n')
max_score = max(scores)
max_score_index = scores.index(max_score)
print(max_score, 'points:')
print(articles[max_score_index].getText())
print(articles[max_score_index].get('href'))
