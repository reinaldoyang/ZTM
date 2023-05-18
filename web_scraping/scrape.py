import requests
from bs4 import BeautifulSoup
import pprint

#get request to get information
res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
#. in the select means that it's a class
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hackernews_list):
    return sorted(hackernews_list, key= lambda k:k['votes'], reverse = True)

def create_custom_hackernews(links, subtext):
    hackerNews = []
    for i, item in enumerate(links):
        #get the text inside the tag
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hackerNews.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hackerNews)

pprint.pprint(create_custom_hackernews(mega_links, mega_subtext))