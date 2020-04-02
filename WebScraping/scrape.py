import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(flinks, fsubtext):
    hn = []
    for idx, item in enumerate(flinks):
        title = flinks[idx].getText()
        href = flinks[idx].get('href', None)
        vote = fsubtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def sort_stories_by_votes(hnList):
    return sorted(hnList, key = lambda k:k['votes'], reverse=True)


pprint.pprint(create_custom_hn(links, subtext))

# print(soup.select('.storylink'))
# print(soup.select('#score_22748135'))
# print(soup.select('.score'))
