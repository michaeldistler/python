import requests
import bs4

root_url = 'http://pyvideo.org'
index_url = root_url + '/category/50/pycon-us-2014'


def get_article_urls():
    response = requests.get(index_url)
    print response

print get_article_urls()
