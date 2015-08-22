# Web Scraper to grab names, address, and phone numbers from yellow pages
# Only to be used for practice

from sys import argv
import requests
from bs4 import BeautifulSoup


def make_soup(url):
    r = requests.get(url)
    return BeautifulSoup(r.content)


def scrape_yp_data(url):
    soup = make_soup(url)
    data = soup.find_all("div", {"class": "info"})

    for item in data:
        try:
            print item.contents[0].find_all(
                "a",
                {"class": "business-name"}
            )[0].text
        except:
            pass
        try:
            print item.contents[1].find_all(
                "span",
                {"itemprop": "streetAddress"}
            )[0].text
        except:
            pass
        try:
            print item.contents[1].find_all(
                "span",
                {"itemprop": "addressLocality"}
            )[0].text
        except:
            pass
        try:
            print item.contents[1].find_all(
                "span",
                {"itemprop": "addressRegion"}
            )[0].text
        except:
            pass
        try:
            print item.contents[1].find_all(
                "span",
                {"itemprop": "postalCode"}
            )[0].text
        except:
            pass
        try:
            print item.contents[1].find_all(
                "div",
                {"class": "primary"}
            )[0].text
        except:
            pass


def main():
    if len(argv) > 1:
        url = str(argv[1])
        print scrape_yp_data(url)
    else:
        url = "http://www.yellowpages.com/search?search_terms=computers&geo_location_terms=Louisville%2C+KY"
        print scrape_yp_data(url)


if __name__ == "__main__":
    main()
